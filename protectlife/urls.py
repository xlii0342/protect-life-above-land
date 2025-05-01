from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # 管理后台
    path('admin/', admin.site.urls),
]

# 自动挂载静态文件（使用 settings.STATIC_URL）
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATICFILES_DIRS[0]
)

# SPA 前端入口：除了 admin/，其他所有请求都返回 index.html
urlpatterns += [
    re_path(
        r'^(?!admin/).*$',
        TemplateView.as_view(template_name='index.html'),
        name='spa-entry'
    ),
]
