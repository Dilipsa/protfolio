from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# https://docs.djangoproject.com/en/4.2/ref/settings/#secret-key
SECRET_KEY = config(
    "DJANGO_SECRET_KEY",
    default="django-insecure-cisuzp=lyks+3*n=qqdnd-i2s)@g$ql%vyqf=$*54+tr7%$fml",
)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DJANGO_DEBUG", cast=bool, default=True)

ALLOWED_HOSTS = config(
    "DJANGO_ALLOWED_HOSTS",
    cast=lambda v: [s.strip() for s in v.split(',')],
    default="127.0.0.1"
)

# Application definition
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
]

THIRD_PARTY_APPS = [
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "crispy_forms",
    "crispy_bootstrap5",
]

LOCAL_APPS = [
    "users",
]

# https://docs.djangoproject.com/en/4.2/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# https://docs.djangoproject.com/en/4.2/ref/settings/#static-root
STATIC_ROOT = str(BASE_DIR / "staticfiles")

# https://docs.djangoproject.com/en/4.2/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(BASE_DIR / "static")]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# https://docs.djangoproject.com/en/4.2/ref/settings/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# https://docs.djangoproject.com/en/4.2/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"

# https://docs.djangoproject.com/en/4.2/ref/settings/#site-id
SITE_ID = 1

# https://docs.djangoproject.com/en/4.2/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "users:redirect"

EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_USERNAME_REQUIRED = False

# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_AUTHENTICATION_METHOD = config('ACCOUNT_AUTHENTICATION_METHOD', default='username')

# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED = True

# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_VERIFICATION = config('ACCOUNT_EMAIL_VERIFICATION', default='mandatory')

# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_LOGOUT_ON_GET = True

# https://docs.djangoproject.com/en/4.2/topics/email/#smtp-backend
EMAIL_HOST = config('EMAIL_HOST', default="smtp.gmail.com")
EMAIL_PORT = config('EMAIL_PORT', default="587")
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default="")
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default="")


# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
