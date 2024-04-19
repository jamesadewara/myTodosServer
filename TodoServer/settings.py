from pathlib import Path
from os import path as osPath
from decouple import config
from . import juzzmin
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast= bool)

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "jazzmin",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "corsheaders",
    "AuthApi.apps.AuthapiConfig",
    "MainApi.apps.MainapiConfig",
]

# Below template variable
REST_FRAMEWORK = {
   'DEFAULT_AUTHENTICATION_CLASSES': (
     'rest_framework_simplejwt.authentication.JWTAuthentication',
      'rest_framework.authentication.TokenAuthentication',
   ),
   'DEFAULT_PERMISSION_CLASSES': [
      'rest_framework.permissions.IsAuthenticated',
   ]
}

SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
   'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
}

# Configure Djoser settings
DJOSER = {
    'SERIALIZERS': {
        'user_create': 'AuthApi.serializers.AccountUserCreateSerializer',
        'user': 'AuthApi.serializers.AccountUserSerializer',
    },
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'auth/users/activation/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': False,  # Disable Djoser's default activation email
}

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TodoServer.urls'

AUTH_USER_MODEL = "AuthApi.User"

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

WSGI_APPLICATION = 'TodoServer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        "USER": "ProxBar1",
        "PASSWORD": "pro1.pro2.PrO3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = osPath.join(BASE_DIR, "static")

MEDIA_URL = "/media/"

MEDIA_ROOT = osPath.join(BASE_DIR, "media")


#JAZZMIN DESIGNS
JAZZMIN_SETTINGS = juzzmin.JAZZMIN_SETTINGS


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    # Other authentication backends if needed
]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:8000',
]

#CSRF
#CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', cast=bool)

#CSP_INCLUDE_NONCE_IN = ['script-src']

#SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', cast=bool)
#CSP
#CSP_DEFAULT_SRC = ("'self'",)

#CSP_STYLE_SRC = ("'self'",)

#CSP_SCRIPT_SRC = ("'self'",)

#CSP_IMG_SRC = ("'self'",)

#CSP_FONT_SRC = ("'self'",)

#HSTS

#SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', cast=int)


#SECURE_HSTS_INCLUDE_SUBDOMAINS = config('SECURE_HSTS_INCLUDE_SUBDOMAINS', cast=bool)


#SECURE_HSTS_PRELOAD = config('SECURE_HSTS_PRELOAD', cast=bool)

#use https through the website
#SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', cast=bool)

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 465 #587  
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
#EMAIL_USE_TLS = True 
EMAIL_USE_SSL = config("EMAIL_USE_SSL", cast= bool)
DEFAULT_FROM_EMAIL = config("EMAIL_HOST_USER")