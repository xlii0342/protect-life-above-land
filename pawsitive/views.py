

from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from .models import Pet, AdoptionApplication, VolunteerApplication
from .serializers import PetSerializer, AdoptionApplicationSerializer, VolunteerApplicationSerializer

import os

import logging
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



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
logger = logging.getLogger(__name__)

@api_view(['POST'])
def submit_volunteer_application(request):
    try:
        serializer = VolunteerApplicationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        application = serializer.save()

        # 这里省略邮件逻辑，或用前端 EmailJS

        return Response(
            {'status': 'success', 'message': 'Application submitted successfully!'},
            status=status.HTTP_201_CREATED
        )
    except Exception as e:
        logger.exception("submit_volunteer_application failed")
        return Response(
            {'status': 'error', 'message': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )