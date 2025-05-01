from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    # 后台管理
    path('admin/', admin.site.urls),

    # SPA 前端入口，除了 admin/ 外都返回前端 index.html
    re_path(r'^(?!admin/).*$', TemplateView.as_view(template_name='index.html'), name='spa-entry'),
]
