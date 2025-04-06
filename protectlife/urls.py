from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pawsitive.urls')),  # 将根 URL 交由 pawsitive 应用处理
]
