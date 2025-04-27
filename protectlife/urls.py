from django.conf import settings
from django.urls import path, re_path, include
from django.views.static import serve
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API路由
    path('api/', include('pawsitive.urls')),  # pawsitive应用的API路由
    
    # 静态文件服务
    path('static/<path:path>', serve, {
        'document_root': settings.STATIC_ROOT,
    }),
    
    # Vue路由处理 - 所有非API和静态文件的请求都返回index.html
    re_path(r'^(?!api/|static/).*$', TemplateView.as_view(template_name='index.html')),
]

# 开发环境下的媒体文件服务
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
