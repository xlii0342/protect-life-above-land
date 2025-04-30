from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # 你的其它 API 路由... 例如：
    # path('api/pets/', include('pawsitive.urls'))
]

# 使用 WhiteNoise 来处理静态文件，无需手动调用 django.views.static.serve
# collectstatic 后，静态文件都在 STATIC_ROOT（staticfiles）里

# 1) 为 debug 模式下提供静态文件访问（Heroku 上由 WhiteNoise 管理）
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATICFILES_DIRS[0]
    )

# 2) favicon.ico 单独路由（可选）
urlpatterns += [
    re_path(r'^favicon\.ico$',
        TemplateView.as_view(template_name='vue_static/favicon.ico'),
        name='favicon'
    ),
]

# 3) 通配所有非 /static/ 及非 /admin/ 的请求，返回前端 SPA 的入口 index.html
urlpatterns += [
    re_path(r'^(?!static/|admin/).*$',
        TemplateView.as_view(template_name='vue_static/index.html'),
        name='spa-entry'
    ),
]
