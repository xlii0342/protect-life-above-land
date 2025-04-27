# from django.shortcuts import render

# def home(request):
#     return render(request, 'home.html')

# def petowner(request):
#     return render(request, 'PetOwner.html')

# def roy(request):
#     return render(request, 'roy.html') 

# def learn(request):
#     return render(request, 'learn.html')

# def map(request):
#     return render(request, 'map.html')

# def report(request):
#     return render(request, 'report.html')

# def support(request):
#     return render(request, 'support.html')

from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
# from twilio.rest import Client  # 暂时注释掉，因为现在不需要 SMS 功能
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To, Email, Content
from .models import Pet, AdoptionApplication, VolunteerApplication
from .serializers import PetSerializer, AdoptionApplicationSerializer, VolunteerApplicationSerializer

import os
from datetime import datetime

def vue_app(request):
    vue_index_path = os.path.join(os.path.dirname(__file__), 'vue_static', 'index.html')
    with open(vue_index_path, encoding='utf-8') as f:
        return HttpResponse(f.read())

def submit_form(request):
    return HttpResponse("Form submitted successfully!")

def get_data(request):
    data = {
        "message": "This is data from get_data view!"
    }
    return JsonResponse(data)

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def get_queryset(self):
        queryset = Pet.objects.all()
        species = self.request.query_params.get('species', None)
        status = self.request.query_params.get('status', None)
        
        if species:
            queryset = queryset.filter(species=species)
        if status:
            queryset = queryset.filter(status=status)
            
        return queryset.order_by('-created_at')

class AdoptionApplicationViewSet(viewsets.ModelViewSet):
    queryset = AdoptionApplication.objects.all()
    serializer_class = AdoptionApplicationSerializer

    def create(self, request, *args, **kwargs):
        # 获取相关的宠物
        pet_id = request.data.get('pet')
        pet = get_object_or_404(Pet, id=pet_id)
        
        # 检查宠物是否可领养
        if pet.status != 'AVAILABLE':
            return Response(
                {'error': 'This pet is not available for adoption'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # 创建申请
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # 更新宠物状态
        pet.status = 'PENDING'
        pet.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def process_application(self, request, pk=None):
        application = self.get_object()
        new_status = request.data.get('status')
        
        if new_status not in ['APPROVED', 'REJECTED']:
            return Response(
                {'error': 'Invalid status'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # 更新申请状态
        application.status = new_status
        application.save()
        
        # 更新宠物状态
        pet = application.pet
        if new_status == 'APPROVED':
            pet.status = 'ADOPTED'
            # 拒绝该宠物的其他申请
            AdoptionApplication.objects.filter(
                pet=pet,
                status='PENDING'
            ).exclude(id=application.id).update(status='REJECTED')
        elif new_status == 'REJECTED' and pet.status == 'PENDING':
            # 如果没有其他待处理的申请，将宠物状态改回可领养
            if not pet.applications.filter(status='PENDING').exists():
                pet.status = 'AVAILABLE'
        pet.save()
        
        return Response({'status': 'success'})

@api_view(['POST'])
def submit_volunteer_application(request):
    serializer = VolunteerApplicationSerializer(data=request.data)
    if serializer.is_valid():
        application = serializer.save()
        
        try:
            # 准备 SendGrid 邮件数据
            dynamic_template_data = {
                'volunteer_name': application.name,
                'submitted_date': application.created_at.strftime("%B %d, %Y"),
                'opportunities': application.experience,  # 或其他相关字段
                'availability': application.availability
            }

            # 创建 SendGrid 邮件
            message = Mail(
                from_email=Email(settings.DEFAULT_FROM_EMAIL),
                to_emails=To(application.email)
            )
            
            # 设置模板 ID（需要替换为你的实际模板 ID）
            message.template_id = 'd-your-template-id'  # 替换为你的 SendGrid 模板 ID
            message.dynamic_template_data = dynamic_template_data

            # 发送邮件
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)

            return Response({
                'status': 'success',
                'message': 'Application submitted successfully! Please check your email for confirmation.'
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            # 记录错误但仍然返回成功（因为申请已保存）
            print(f"Failed to send email: {str(e)}")
            return Response({
                'status': 'success',
                'message': 'Application submitted successfully, but there was an issue sending the confirmation email. Our team will contact you soon.'
            }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)