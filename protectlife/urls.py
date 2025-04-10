# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('pawsitive.urls')),  
# ]

from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # 所有 URL 均返回前端 Vue SPA 的入口页面
    re_path(r'^.*$', TemplateView.as_view(template_name='vue_static/index.html')),
]

