from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # 其他API或应用路由...
]

# 让 Django 处理静态资源
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

# 最后添加 catch-all 规则，返回 Vue 的 index.html
urlpatterns += [
    re_path(r'^.*$', TemplateView.as_view(template_name="index.html")),
]
