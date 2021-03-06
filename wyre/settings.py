"""
Django settings for wyre project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os, pytz
import socket
from google.oauth2 import service_account

try:
    HOSTNAME = socket.gethostname()
except:
    HOSTNAME = 'localhost'



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/auth/login'
LOGIN_URL = '/auth/login'

CACHE_EXPIRY = 1800

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hdhw*b6jko0m!@8@j8ufk+1ybj8u#gc@4ov0_xec((exhar=io'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  if HOSTNAME == "DESKTOP-U00EROM" else False
# DEBUG = True

ALLOWED_HOSTS = ['wyre.pythonanywhere.com',
                'localhost',
                "www.wyreng.com",
                "wyreng.com",
                "104.197.70.223",
                "35.239.28.105",
                "34.69.115.137"
                ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'main',
    'useraccounts'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wyre.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'wyre.wsgi.application'
# DATA_UPLOAD_MAX_NUMBER_FIELDS = None

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

if HOSTNAME !=  'DESKTOP-U00EROM':
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.mysql',
    #         'OPTIONS': {
    #             'sql_mode': 'traditional',
    #         },
    #         'NAME': 'wyre$wyre_app_db',
    #         'USER': 'wyre',
    #         'PASSWORD': 'wyre_db_password_new',
    #         'HOST': 'wyre.mysql.pythonanywhere-services.com',
    #     }
    # }
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'sql_mode': 'traditional',
            },
            'NAME': 'wyredb',
            'USER': 'wyreuser',
            'PASSWORD': '11111111',
            'HOST': 'localhost',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

# STATIC_DIR = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

lagos_tz = pytz.timezone("UTC")

if HOSTNAME == "DESKTOP-U00EROM":#USING WHITENOISE FOR STATIC

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFileStorage'

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

else: #USING GCLOUDS STORAGE FOR BOTH MEDIA AND STATIC
    DEFAULT_FILE_STORAGE = 'wyre.gcloud_storages.GoogleCloudMediaStorage'
    STATICFILES_STORAGE = 'wyre.gcloud_storages.GoogleCloudStaticStorage'
    GS_BUCKET_NAME = 'wyre_cdn'
    GS_PROJECT_ID = 'project-id'
    GS_DEFAULT_ACL = 'publicRead'

    # GOOGLE_APPLICATION_CREDENTIALS = 'C:\\Users\\INYANG\\Desktop\\MyFirstProject-d58e02069744.json'
    # GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    #     GOOGLE_APPLICATION_CREDENTIALS
    # )
    GOOGLE_APPLICATION_CREDENTIALS = '/home/Linux/My First Project-64c9e2b7b1b2.json'
    GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
        GOOGLE_APPLICATION_CREDENTIALS
    )
    
    MEDIA_URL = '/media/'
    MEDIA_ROOT = DEFAULT_FILE_STORAGE
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


