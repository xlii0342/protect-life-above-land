import os
from pathlib import Path
import dj_database_url  # 如果不需要可删除

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "your_secret_key_here"
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "pawsitive",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # 用于生产环境根路径静态服务
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "protectlife.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'frontend' / 'Iteration2' / 'vue_static'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "protectlife.wsgi.application"

# 数据库配置
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600)
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ——— 静态 & 媒体 文件 配置 ———

# 1. 静态文件 根路径（去除 /static/ 前缀）
STATIC_URL = '/'
STATICFILES_DIRS = [
    BASE_DIR / 'frontend' / 'Iteration2' / 'vue_static'
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# 2. 媒体文件 前缀（与 STATIC_URL 保持不同）
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 3. WhiteNoise 存储配置（生产环境使用）
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ——— 其它配置 ———

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
