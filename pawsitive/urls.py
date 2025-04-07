from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Home.html', views.home, name='home'),
    path('PetOwner.html', views.petowner, name='petowner'),
    path('Roy.html', views.roy, name='roy'),
    path('Learn.html', views.learn, name='learn'),
    path('Map.html', views.map, name='map'),
    path('Report.html', views.report, name='report'),
    path('Support.html', views.support, name='support'),
]
