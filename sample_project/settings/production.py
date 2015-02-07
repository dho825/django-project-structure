"""
Django settings for sample_project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/

dho825 note: make sure to still generate a sample project from the
latest version of Django with manage.py startproject and use this as a reference point
to compare with what your configurations
"""

import os, sys
from django.utils.crypto import get_random_string

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
APPS_DIR = os.path.join(BASE_DIR, 'apps')
sys.path.insert(0, BASE_DIR)
sys.path.insert(1, APPS_DIR)
sys.path.insert(2, os.path.join(BASE_DIR, 'libs'))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# ROOT_PATH = os.path.dirname(__file__)
ROOT_URLCONF = 'sample_project.urls'
WSGI_APPLICATION = 'sample_project.wsgi.application'

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    # os.path.join(ROOT_PATH, 'templates'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '=d5&vdw&b!2+a5lieo&#050p=)qnjps@b*3s@h^n2^h&8oc4fh'
# A secret key used for cryptographic algorithms.
SECRET_KEY = os.environ.get("SECRET_KEY", get_random_string(50, "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"))


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sample_app',
    'another_app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    )),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    # "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
# since Django 1.7 - to remove warning of new test runner for apps created prior to Django 1.7

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# change this depending on what server/production DB you're using

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}