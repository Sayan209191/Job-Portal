from pathlib import Path
import os
import pymysql

pymysql.version_info = (1,4,6,'final',0) 
pymysql.install_as_MySQLdb()
# from pymongo import MongoClient
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=_k+dwt!n6$hinlrk#rt(dul5(x7g-u0gm$6fr8$vz@6whqj9y'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='makeyourcareer.helpdesk@gmail.com'
EMAIL_HOST_PASSWORD='ljes rvru vmdn waor'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_USE_SSL = False  
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    "widget_tweaks",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',   
    'myapp',   
    'accounts',
    'jobs',
    'blog',
    'allauth',   
    'allauth.account',  
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # 'CustomSocialAccount'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]


# Session settings
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_NAME = 'sessionid'
SESSION_COOKIE_AGE = 1209600  # 2 weeks
SESSION_SAVE_EVERY_REQUEST = False
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

ROOT_URLCONF = 'jobportal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['template'],
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

WSGI_APPLICATION = 'jobportal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jobportal',
        'USER' : 'testuser',
        'PASSWORD' : 'Sayan@1234',
        'HOST' : '192.168.1.6', #192.168.84.202 #192.168.146.202 
        'PORT' : '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

# SOCIALACCOUNT_MODELS = {
#     "socialaccount.SocialAccount": {
#         "extra_data": {"type": "dict", "default": {}}
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'ENFORCE_SCHEMA': False,
#         'CLIENT': {
#             'host': 'mongodb+srv://sayan:sayan@makeyourcareer.haskg.mongodb.net/?retryWrites=true&w=majority&appName=MAKEYOURCAREER',
#             'port': 27017,              
#             'username': 'sayan', 
#             'password': 'sayan',
#             # 'authSource': 'admin',
#             # 'authmechnishm': 'SCRAM-SHA-1',
#         },
#         'NAME': 'MAKEYOURCAREER',
#     }
# }

# client = MongoClient("mongodb+srv://sayan:sayan@makeyourcareer.haskg.mongodb.net/?retryWrites=true&w=majority&appName=MAKEYOURCAREER")
# db = client['sayan']

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


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


SITE_ID = 2
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_EMAIL_VERIFICATION = "none"

SOCIALACCOUNT_LOGIN_ON_GET = True

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,

    }
}


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    os.path.join(BASE_DIR, "static")    
]
STATIC_ROOT = os.path.join(BASE_DIR,'/static/')

# media file configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# enable logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}


JAZZMIN_SETTINGS = {
    'site_header':"MAKE YOUR CAREER",
    'site_brand' : "MAKE YOUR CAREER",
    'copyright' : "@Make Your Career",
}
JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
}
