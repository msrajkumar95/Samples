import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c(_=(x7qzw!s4d$w9_3e-hda8ke*tvr6yp@#qlzxt+s6$o!&tw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.raju.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'accounts',
    'home',
    'rest_framework',
    'quickstart.apps.QuickstartConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Tutorial.middleware.LoginRequiredMiddleware'
]

ROOT_URLCONF = 'Tutorial.urls'

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

WSGI_APPLICATION = 'Tutorial.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tutorial',
        'USER': 'msrajkumar95',
        'HOST': 'localhost',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
    'accounts.backends.EmailBackend',
    'accounts.backends.UsernameBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'accounts/static/accounts/media')

LOGIN_REDIRECT_URL = '/home/'

LOGIN_URL = '/account/login/'

LOGIN_EXEMPT_URLS = (
    r'account/logout/',
    r'account/register/',
    r'account/reset-password/',
    r'account/reset-password/done/',
    r'account/reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/',
    r'account/reset-password/complete/'
)

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# run < python -m smtpd -n -c DebuggingServer localhost:1025 > in cmd to create smtp server
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025

# http://sems.sas.com/bess/get?id=-108606.-5:-hx1ybsml:rzzb.1erfcbafrf0&RZNVY=ebanyq.sbafrpn@fnf.pbz&nccvq=41315

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'djangoframework21@gmail.com'
EMAIL_HOST_PASSWORD = 'ms8438440068'
EMAIL_USE_TLS = True
EMAIL_PORT = '587'
