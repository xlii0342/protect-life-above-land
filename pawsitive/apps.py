from django.apps import AppConfig
import os
import psycopg2
from django.db import connections

class PawsitiveConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pawsitive"

# 使用 Django 的 settings.py 配置数据库
DATABASE_URL = os.environ.get("DATABASE_URL")

# 解析 DATABASE_URL
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL)
}
