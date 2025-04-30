from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.http import HttpResponseNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    # 你的其它 API 路由... 例如：
    # path('api/pets/', include('pawsitive.urls'))
]

# 1) Debug 模式下提供静态文件访问
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATICFILES_DIRS[0]
    )

# 2) favicon.ico 单独处理（可选）
urlpatterns += [
    re_path(r'^favicon\.ico$',
        serve,
        {
            'document_root': settings.STATICFILES_DIRS[0],
            'path': 'favicon.ico'
        },
        name='favicon'
    ),
]

# 3) 匹配所有非 static/admin 的路径，返回 index.html，支持前端 Vue Router 刷新
urlpatterns += [
    re_path(r'^(?!static/|admin/).*$',
        serve,
        {
            'document_root': settings.STATICFILES_DIRS[0],
            'path': 'index.html'
        },
        name='spa-entry'
    ),
]



urlpatterns += [
    re_path(r'^static/$', lambda request: HttpResponseNotFound("Direct access to /static/ is not allowed."))
]
