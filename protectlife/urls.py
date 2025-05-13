from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from pawsitive.views import submit_volunteer_application


urlpatterns = [
    # 后台管理
    path('admin/', admin.site.urls),

    path(
      'api/volunteer/',
      csrf_exempt(submit_volunteer_application),
      name='volunteer-apply'
    ),

    # SPA 前端入口，除了 admin/ 外都返回前端 index.html
    re_path(r'^(?!admin/).*$', TemplateView.as_view(template_name='index.html'), name='spa-entry'),
]
