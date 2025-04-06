from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),        
    path('Learn.html', views.learn, name='learn'),   
    path('Map.html', views.map_view, name='map'),    
    path('Report.html', views.report, name='report'),
    path('Support.html', views.support, name='support'),
    path('Roy.html', views.support, name='support'),
]
