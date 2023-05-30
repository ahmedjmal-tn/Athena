"""
Django settings for Athena project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

import environ
env=environ.Env()
environ.Env.read_env()
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-7w+snsw721fr)i@*m^vap2t$q++ch2ap6o6tq!qe980hwq=s(r"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "dashboard.apps.DashboardConfig",
    "authentification.apps.AuthentificationConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "social_django",
    "Article",
    "Produit",
    "ckeditor",
    "notifications",
    "django.contrib.humanize",
    "captcha",
    "Magazine",
    "django.contrib.sites",  # must
    "allauth",  # must
    "allauth.account",  # must
    "allauth.socialaccount",  # must
    "allauth.socialaccount.providers.google",  # new
    "allauth.socialaccount.providers.facebook",
    "Market",
    "payments.apps.PaymentsConfig",  # new
    "Analyse",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Athena.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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


WSGI_APPLICATION = "Athena.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'athenadb',
        'USER': 'athena',
        'PASSWORD': 'athena',
        'HOST': 'localhost',
        'PORT': '5432',


    }
}
"""
import dj_database_url
DATABASES = {
    'default':dj_database_url.parse(env('Database_URL'))

}
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "Athena\static")]

LOGIN_REDIRECT_URL = "/"

# MEDIA
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
RECAPTCHA_PUBLIC_KEY = "6LcJS_8kAAAAALlLOKcAAUZPBgItzT_A-XWosRjx"
RECAPTCHA_PRIVATE_KEY = "6LcJS_8kAAAAABQkOTqzAkKWivESkS5tyRiG5rMP"
RECAPTCHA_REQUIRED_SCORE = 0.85
SOCIAL_AUTH_FACEBOOK_KEY = "532074388796071"  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = "09f5e96a4be8acb6b12b3e19fc5907b4"  # App Secret


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "djingoproject@gmail.com"
EMAIL_HOST_PASSWORD = "buknsdfwlavrkjzo"
# password mail django : 123456django


# core/settings.py

SITE_ID = 1
SOCIALACCOUNT_LOGIN_ON_GET = True
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    #'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
    "Athena.backends.EmailBackend",
]

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    }
}

ACCOUNT_EMAIL_VERIFICATION = "none"

LOGIN_REDIRECT_URL = "/"
# settings.py

CKEDITOR_CONFIGS = {
    "default": {
        "height": 300,
        "width": "100%",
    }
}


STRIPE_PUBLISHABLE_KEY = "pk_test_51N5rPuFKWJoO9geeE6epbl5M2wZG0pI1o0NrlLVZvki1AmunuvfEa7tFZAX3Lm2fDA9E1vTMZCuxtN4TAZOPTlkd00cdZbxhpM"
STRIPE_SECRET_KEY = "sk_test_51N5rPuFKWJoO9geeXE8KjlfoOh4zrGThUiOIfAb3n9l41J8CD6jUv0745QSYWekpx1fYOreoyXqkSSSoD7oCkCy600YA2eAxwX"
