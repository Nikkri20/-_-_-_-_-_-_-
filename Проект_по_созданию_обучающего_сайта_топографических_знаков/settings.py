"""
Django settings for Проект_по_созданию_обучающего_сайта_топографических_знаков project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import environ
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

env = environ.Env(
    ALLOWED_HOSTS=(list, [])
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ['DEBUG'].lower() in ['true', '1']

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app1',
    'django_cleanup.apps.CleanupConfig',
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

ROOT_URLCONF = 'Проект_по_созданию_обучающего_сайта_топографических_знаков.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Проект_по_созданию_обучающего_сайта_топографических_знаков.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if DEBUG:
    DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': env('POSTGRES_ENGINE'),
            'NAME': env('POSTGRES_NAME_DB'),
            'USER': env('POSTGRES_USER'),
            'PASSWORD': env('POSTGRES_PASSWORD'),
            'HOST': env('POSTGRES_HOST'),
            'PORT': env('POSTGRES_PORT'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'RU-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

if DEBUG:
    STATIC_URL = 'static/'
    STATICFILES_DIRS = [
        BASE_DIR / "static",
        "./static"
    ]
    MEDIA_ROOT = os.path.join(BASE_DIR, '/static/')
    MEDIA_URL = '/images/'
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles/images/')
    MEDIA_URL = '/images/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# информация о почте

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = eval(env('EMAIL_USE_TLS'))
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = eval(env('EMAIL_USE_SSL'))