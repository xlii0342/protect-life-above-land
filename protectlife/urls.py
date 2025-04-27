from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 静态文件服务
    re_path(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT,
    }),
    
    # Vue路由处理
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]

# 开发环境下的静态文件和媒体文件服务
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
