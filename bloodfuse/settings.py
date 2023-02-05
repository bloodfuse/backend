# Import os module
from bloodfuse.env import load_env
from corsheaders.defaults import default_headers
import os
from pathlib import Path
from datetime import timedelta
import uuid

# dotenv.load_dotenv("
load_env()

#  Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE = BASE_DIR / 'db.sqlite3'
TEMPLATE = BASE_DIR / 'templates'
STATIC = BASE_DIR / 'static/'
MEDIA = BASE_DIR / 'd56ns165tm1d65sg1j65h1fdbd'

# .env imports
MODE = os.getenv("mode")
Database = os.getenv("database")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.getenv("APP_SECRET_KEY")
SECRET_KEY = os.getenv("secret_key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.getenv("debug_status")))

ALLOWED_HOSTS = os.getenv("allowed_hosts").split(",")


# Application definition

DEFAULT_INSTALLED_APPS = [
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
ADDED_INSTALLED_APPS = ['jazzmin']

if MODE != 'production':
    INSTALLED_APPS = DEFAULT_INSTALLED_APPS
else:
    INSTALLED_APPS = ADDED_INSTALLED_APPS + DEFAULT_INSTALLED_APPS
    JAZZMIN_SETTINGS = {
        "site_title": "BloodFuse DJango Admin",
        "site_header": "BloodFuse",
        "site_brand": "BloodFuse",
        "copyright": "BloodFuse Ltd",
        "welcome_sign": "Welcome to BloodFuse Django Admin",
    }
    JAZZMIN_UI_TWEAKS = {
        "theme": "simplex",
        'dark_mode_theme': "darkly"

    }

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

if Database == 'sqlite3':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': DATABASE,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv("DB_NAME"),
            'USER': os.getenv("DB_USER"),
            'PASSWORD': os.getenv("DB_PASSWORD"),
            'HOST': os.getenv("DB_HOST"),
            'PORT': os.getenv("DB_PORT"),
        }
    }


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
# EMAIL_PORT = env.get("EMAIL_PORT")
# EMAIL_HOST_USER = env.get("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env.get("EMAIL_HOST_PASSWORD")


# _________________________________________________________________________________________
# SWAGGER
# _________________________________________________________________________________________


# _________________________________________________________________________________________
# CORS
# _________________________________________________________________________________________
CORS_ALLOWED_ORIGINS = os.getenv("cors_allowed_hosts").split(",")

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = list(default_headers)
# CORS_ALLOW_HEADERS = list(default_headers) + [
#     'Access-Control-Allow-Origin',
# ]


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
# LOGIN_URL = 'https://bloodfuse.pythonanywhere.com/api/auth/login' # Old Login Url
# LOGIN_URL = 'shark-app-49nyv.ondigitalocean.app/api/auth/login'  # New Login Url
# LOGIN_URL = 'https://api.bloodfuse.com/api/auth/login/'  # New Login Url
if MODE != 'production':
    LOGIN_URL = 'http://localhost:3873/api/auth/login'
else:
    LOGIN_URL = os.getenv("login_url")  # New Login Url


# _________________________________________________________________________________________
# DJ-REST-AUTH
# _________________________________________________________________________________________

REST_USE_JWT = True
JWT_AUTH_COOKIE = 'bloodfuse'  # The cookie key name can be the one you want
JWT_AUTH_REFRESH_COOKIES = 'parser'
JWT_AUTH_SECURE = False
JWT_AUTH_HTTPONLY = True
JWT_AUTH_SAMESITE = 'Lax'

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
# THEVARIABLE = os.getenv("SAVED")

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
if MODE == 'production':
    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(hours=2)
    }
else:
    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=1)
        # 'ACCESS_TOKEN_LIFETIME': timedelta(hours=int(os.getenv("dev_token_lifetime")))
    }


# _________________________________________________________________________________________
# PERSONAL SETTINGS
# _________________________________________________________________________________________
