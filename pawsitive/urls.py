from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'pets', views.PetViewSet)
router.register(r'applications', views.AdoptionApplicationViewSet)

app_name = 'pawsitive'

urlpatterns = [
    path('', include(router.urls)),
    path('volunteer/', views.submit_volunteer_application, name='submit_volunteer'),
]

