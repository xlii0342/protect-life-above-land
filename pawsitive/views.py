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
# from twilio.rest import Client  # Commenting out Twilio for now
from .models import Pet, AdoptionApplication, VolunteerApplication
from .serializers import PetSerializer, AdoptionApplicationSerializer, VolunteerApplicationSerializer

import os

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
        
        # 构建邮件内容
        try:
            # 发送给申请者的确认邮件
            subject = 'Welcome to Protect Life Above Land - Volunteer Application Received'
            message = f'''Dear {application.name},

Thank you for your interest in volunteering with Protect Life Above Land! We are excited about your commitment to protecting Victoria's native species and natural environment.

Your Application Details:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Name: {application.name}
• Email: {application.email}
• Phone: {application.phone}
• Availability: {application.availability}

Your Experience & Skills:
{application.experience}

What Happens Next:
1. Our volunteer coordinator will review your application within 2-3 business days
2. You will receive an email invitation for an online orientation session
3. After the orientation, we will match you with suitable volunteer opportunities

Important Information:
- Please add noreply@protectlife.com to your email contacts
- Check your spam folder if you don't receive our follow-up email
- For any questions, please contact us at support@protectlife.com

We truly appreciate your willingness to contribute to our mission of protecting endangered species and their habitats.

Best regards,
The Protect Life Above Land Team
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
This is an automated message, please do not reply to this email.'''

            # 发送邮件
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [application.email],
                fail_silently=False,
            )

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