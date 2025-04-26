from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),

    # —— ① 专门处理 /static/ 路径 ——  
    re_path(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.STATICFILES_DIRS[0],
    }),

    # —— ② 根路径首页 ——  
    re_path(r'^$', serve, {
        'path': 'index.html',
        'document_root': settings.STATICFILES_DIRS[0],
    }),

    # —— ③ 其余请求都返回 index.html ——  
    re_path(r'^(?P<path>.*)$', serve, {
        'document_root': settings.STATICFILES_DIRS[0],
    }),
]

# （如果 DEBUG=True 需要同时暴露 media）
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
