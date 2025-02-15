from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get("SECRET_KEY")


DEBUG = os.environ.get("DEBUG", "False").lower() == "true"


ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")




# SECRET_KEY = 'django-insecure-#lpyxfbgvu(yzw7md1dn8slhht06@m=^j)$m#*%_f&4n^vse!v'

# DEBUG = True

# ALLOWED_HOSTS = []



INSTALLED_APPS = [
    
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',
    'home.apps.HomeConfig',
    'about.apps.AboutConfig',
    'blog.apps.BlogConfig',
    'gallery.apps.GalleryConfig',
    'shop.apps.ShopConfig',
    'contact.apps.ContactConfig',
    'account.apps.AccountConfig',
    
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

ROOT_URLCONF = 'iqnaax.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'iqnaax.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [

#     os.path.join(BASE_DIR, 'home/static')
# ]


# if not DEBUG:
    # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.
    # STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_ROOT = BASE_DIR / 'staticfiles'

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



    
# STATICFILES_DIRS=[os.path.join(BASE_DIR,"static"), "templates"]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/profile/'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SESSION_ENGINE = "django.contrib.sessions.backends.db"

TINYMCE_DEFAULT_CONFIG = {
    'height': 500,
    'width': 572,
    'menubar': True,
    'plugins': 'advlist autolink link image lists charmap print preview',
    'toolbar': 'styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image',
    'content_css': [
        '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
        '/static/css/custom_tinymce.css',  
    ],
    'image_advtab': True,
}

JAZZMIN_SETTINGS = {
    "welcome_sign" : "Welcome to IQNAAX Admin",
  
}





