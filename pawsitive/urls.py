# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('Home.html', views.home, name='home'),
#     path('PetOwner.html', views.petowner, name='petowner'),
#     path('Roy.html', views.roy, name='roy'),
#     path('Learn.html', views.learn, name='learn'),
#     path('Map.html', views.map, name='map'),
#     path('Report.html', views.report, name='report'),
#     path('Support.html', views.support, name='support'),
# ]
from django.urls import re_path
from django.views.generic import TemplateView

urlpatterns = [
    re_path(r'^.*$', TemplateView.as_view(template_name="vue_static/index.html")),
]

