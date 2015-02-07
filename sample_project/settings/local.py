"""
Django settings for sample_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from production import BASE_DIR

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Serve static files locally for development
# You may want to use Amazon S3 or some other CDN for static files in production
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}