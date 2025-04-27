from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Vue路由处理 - 确保这是最后一个路由
    re_path(r'^(?!static/).*$', TemplateView.as_view(template_name='index.html')),
]

# 添加静态文件服务
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# 开发环境下的媒体文件服务
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
