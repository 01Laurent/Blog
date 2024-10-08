"""
Django settings for ablog project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2*n_y1w*2hb-+p6y!7^5&rg5y=cv%34ewp2ox0yxj@(q6jankm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myblog',
    'members',
    'django_ckeditor_5',
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

ROOT_URLCONF = 'ablog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ablog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'


CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 400,
        'width': '100%',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'div', 'codesnippet', 'widget', 'lineutils', 'clipboard', 'autogrow'
        ]),
        'removePlugins': 'stylesheetparser',
        'format_tags': 'p;h1;h2;h3;pre',
        'extraAllowedContent': 'div(*);',
        'filebrowserBrowseUrl': '/browser/browse/',
        'filebrowserUploadUrl': '/uploader/upload/',
        'autoGrow_minHeight': 200,
        'autoGrow_maxHeight': 600,
        'autoGrow_bottomSpace': 50,
        'removeButtons': '',
    },
    'basic': {
        'extends': 'default',  # Inherit from 'default'
        'toolbar': [
            {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Underline']},
            {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList']},
            {'name': 'links', 'items': ['Link', 'Unlink']},
            {'name': 'insert', 'items': ['Image', 'Table']},
        ],
        'height': 300,
        'removePlugins': 'elementspath',  # Remove element path plugin
    },
    'standard': {
        'extends': 'default',  # Inherit from 'default'
        'toolbar': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print']},
            {'name': 'clipboard', 'items': ['Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace']},
            {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Strike', 'RemoveFormat']},
            {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert', 'items': ['Image', 'Table', 'HorizontalRule', 'SpecialChar']},
            {'name': 'styles', 'items': ['Styles', 'Format']},
            {'name': 'tools', 'items': ['Maximize']},
        ],
        'height': 450,
        'removeButtons': 'Underline,Subscript,Superscript',
    },
    'custom': {
        'extends': 'default',  # Inherit from 'default'
        'toolbar': [
            {'name': 'clipboard', 'items': ['Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace']},
            {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', 'RemoveFormat']},
            {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert', 'items': ['Image', 'Table', 'HorizontalRule', 'SpecialChar', 'Iframe']},
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
        ],
        'height': 500,
        'width': '80%',
        'removePlugins': 'elementspath',  # Additional plugins removed
    },
    'simple': {
        'extends': 'basic',  # Inherit from 'basic'
        'toolbar': [
            {'name': 'basicstyles', 'items': ['Bold', 'Italic']},
            {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList']},
        ],
        'height': 200,
        'removePlugins': 'toolbar,elementspath',
    },
}

