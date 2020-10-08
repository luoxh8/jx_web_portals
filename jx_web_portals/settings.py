import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'obcoux^#*&^5ew@-niuxn1^8vo*_%ie2m^a0tt@t-5ajl&53b%'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'ckeditor',
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'news.apps.NewsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jx_web_portals.urls'

TEMPLATES = [
    {
        'BACKEND' : 'django.template.backends.django.DjangoTemplates',
        'DIRS'    : [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS' : {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'jx_web_portals.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql',  # 数据库引擎
        'NAME'    : 'jx_web_portals',  # 数据库名，先前创建的
        'USER'    : 'root',  # 用户名，可以自己创建用户
        'PASSWORD': 'TMGz8iILyZoBWpcSRsEl41m7tKwRhPFy',  # 密码
        'HOST'    : '192.168.1.121',  # mysql服务所在的主机ip
        'PORT'    : '3306',  # mysql服务端口
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = '/static/'

# custom
CKEDITOR_UPLOAD_PATH = "uploads/"
