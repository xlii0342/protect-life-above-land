from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 所有路由都返回主页，让Vue.js处理前端路由
    path('', TemplateView.as_view(template_name='index.html')),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]

# DEBUG模式下的media文件服务
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
