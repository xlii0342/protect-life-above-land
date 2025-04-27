from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    # 你其它 API 路由...
]

# 1) 让 /static/xxx.css 或 /static/js/xxx.js 走静态文件目录
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATICFILES_DIRS[0],
)

# 2) 给 favicon.ico 单独处理（可选）
urlpatterns += [
    re_path(r'^favicon\.ico$', serve, {
        'path': 'favicon.ico',
        'document_root': settings.STATICFILES_DIRS[0],
    }),
]

# 3) 最后一个“通配”——把所有剩下的 URL 都返回 index.html
#    这样前端路由才能在浏览器端生效
urlpatterns += [
    re_path(r'^(?!static/).*$',
        serve,
        {
            'document_root': settings.STATICFILES_DIRS[0],
            'path': 'index.html'
        }
    ),
]
