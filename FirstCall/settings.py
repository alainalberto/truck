"""
Django settings for FirstCall project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import socket

from django.core.urlresolvers import reverse_lazy
from django.contrib.messages import constants as messages


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o*&&#z_i@5cmck_-xh8n84wywwp%bmypco2^-#3(^z((69z)2v'

# SECURITY WARNING: don't run with debug turned on in production!
if socket.gethostname() == 'LAPTOP-RQJ5DVKQ':
    DEBUG = True
    ALLOWED_HOSTS = []
else:
    DEBUG = True
    ALLOWED_HOSTS = ['www.fcintermodal.com']


# Application definition

INSTALLED_APPS = [
    #DJango Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django.contrib.sites',
   # 'django.contrib.flatpages',
    'django.contrib.humanize',

    #My Apps
    'apps.tools',
    'apps.accounting',
    'apps.logistic',
    'apps.services',

    #External
    'django_tables2',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'FirstCall.urls'

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'FirstCall.wsgi.application'

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'first_call_db',
        'USER': 'administrator',
        'PASSWORD': 'admin*2017',
        'HOST': 'localhost',
        'PORT': '5432',
        }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGOUT_REDIRECT_URL = reverse_lazy('login')


#ADMINS = (
#('Alain Alberto', 'alainalberto03@gmail.com'),
#('Ransel Ramos ', 'ranselr@gmail.com'),
#)

#MANAGERS = (
#('Alain Alberto', 'alainalberto03@gmail.com'),
#('Ransel Ramos ', 'ranselr@gmail.com'),
#)


#EMAIL_USE_TLS = True
#EMAIL_HOST = ''
#EMAIL_PORT = 25
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackrend'
#EMAIL_SUBJECT_PREFIX = 'ERROR-FIRSTCALL'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

