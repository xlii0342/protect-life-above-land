from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Home.html', views.home, name='home'),     
    path('PetOwner.html', views.petowner, name='petowner'),
    path('Roy.html', views.roy, name='roy'),
]
