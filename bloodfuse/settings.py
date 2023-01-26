# Import os module
from corsheaders.defaults import default_headers
import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE = BASE_DIR / 'db.sqlite3'
TEMPLATE = BASE_DIR / 'templates'
STATIC = BASE_DIR / 'static/'
MEDIA = BASE_DIR / 'd56ns165tm1d65sg1j65h1fdbd'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('APP_SECRET_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = [
    # Localhost
    'localhost',
    '127.0.0.1',
    # Python Everywhere {deprecated}
    'bloodfuse.pythonanywhere.com',
    # Digital Ocean Server {deprecated}
    'shark-app-49nyv.ondigitalocean.app',
    # AWS Server {Main Server}
    '100.25.191.221',
    'ec2-100-25-191-221.compute-1.amazonaws.com',
    'api.ec2-100-25-191-221.compute-1.amazonaws.com',
    'api.bloodfuse.com',
    # AWS Server {Test Server}
    "52.91.128.102",
    'ec2-52-91-128-102.compute-1.amazonaws.com',
    'api.ec2-52-91-128-102.compute-1.amazonaws.com',
    'backend.testnet.bloodfuse.com',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps
    'core',
    'appointments',
    'reports.apps.ReportsConfig',
    'endpoint.apps.EndpointConfig',

    # 3rd Parties
    'corsheaders',
    'drf_yasg',  # endpoint docs
    'rest_framework_simplejwt',  # jwt token

    'dj_rest_auth',  # dj_rest-auth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',

    # Restframe work
    'rest_framework',
    'rest_framework.authtoken',
]

SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bloodfuse.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE],
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

WSGI_APPLICATION = 'bloodfuse.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE,
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#         'HOST': os.environ.get('DB_HOST'),
#         'PORT': os.environ.get('DB_PORT'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


STATIC_URL = 'static/'
STATIC_ROOT = STATIC

MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# _________________________________________________________________________________________
# EMAIL CONFIG
# _________________________________________________________________________________________


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
# * USE THE CONFIGS BELOW FOR PRODUCTION
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'your.email.host'
# EMAIL_PORT = env.get('EMAIL_PORT')
# EMAIL_HOST_USER = env.get('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = env.get('EMAIL_HOST_PASSWORD')


# _________________________________________________________________________________________
# SWAGGER
# _________________________________________________________________________________________


# _________________________________________________________________________________________
# CORS
# _________________________________________________________________________________________
CORS_ALLOWED_ORIGINS = [
    # mainNet
    "https://www.bloodfuse.com",
    "https://bloodfuse.com",
    # testNet
    "https://frontend.testnet.bloodfuse.com",
    "https://admin.testnet.bloodfuse.com",
    # local dev
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = list(default_headers) + [
    'Access-Control-Allow-Origin',
]

# CORS_ALLOW_HEADERS = [
#     "accept",
#     "accept-encoding",
#     "authorization",
#     "content-type",
#     "dnt",
#     "origin",
#     "user-agent",
#     "x-csrftoken",
#     "x-requested-with",
#     "Access-Control-Allow-Credentials",
# ]

# CORS_ALLOW_ALL_ORIGIN = True

# ===== Requsted by fronend devs =====
SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = True

CSRFTOKEN_COOKIE_SAMESITE = 'None'
CSRFTOKEN_COOKIE_SECURE = True

# ==== alternatively ====
CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SECURE = True

MY_APP_AUTH_COOKIE_SAMESITE = 'None'
MY_APP_AUTH_COOKIE_SAMESITE = True
MY_APP_AUTH_COOKIE_SECURE = True


# _________________________________________________________________________________________
# AUTH
# _________________________________________________________________________________________
AUTH_USER_MODEL = "core.User"
# LOGIN_URL = 'http://localhost:8000/api/auth/login'
# LOGIN_URL = 'https://bloodfuse.pythonanywhere.com/api/auth/login' # Old Login Url
LOGIN_URL = 'shark-app-49nyv.ondigitalocean.app/api/auth/login'  # New Login Url

# _________________________________________________________________________________________
# DJ-REST-AUTH
# _________________________________________________________________________________________

REST_USE_JWT = True
JWT_AUTH_COOKIE = 'my-app-auth'  # The cookie key name can be the one you want

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_EMAIL_VERIFICATION = 'none'
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True

REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'core.serializers.UserLoginSerializer',
}

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'core.serializers.UserRegisterSerializer'
}

# GLOBAL VARIABLES
# THEVARIABLE = os.environ.get('SAVED')

# _________________________________________________________________________________________
# SIMPLE_JWT
# _________________________________________________________________________________________
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     )
# }
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
}

# SIMPLE JWT
if os.environ.get('MODE') == 'production':
    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(hours=2)
    }
else:
    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(hours=24)
    }


# _________________________________________________________________________________________
# PERSONAL SETTINGS
# _________________________________________________________________________________________
