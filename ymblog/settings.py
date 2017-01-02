# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0t1z6qr^r_dud+7zn3b4t!t9n+sw#xugv=ec+m$x^=pd0$kxft'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['blog.hnsichuang.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
)

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'ymblog.urls'

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

WSGI_APPLICATION = 'ymblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ymblog',
        'USER':'ym',
        'PASSWORD':'panyuli1314520',
        'HOST':'127.0.0.1',
        'PORT':'5432',
    }
}


CKEDITOR_CONFIGS = {
    'default': {
		'language' : 'zh-cn',
        'toolbar': (
            ['CodeSnippet', ],
            ['div','Source','-','Save','NewPage','Preview','-','Templates'], 
            ['Cut','Copy','Paste','PasteText','PasteFromWord','-','Print','SpellChecker','Scayt'], 
            ['Undo','Redo','-','Find','Replace','-','SelectAll','RemoveFormat'], 
            ['Form','Checkbox','Radio','TextField','Textarea','Select','Button', 'ImageButton','HiddenField'], 
            ['Bold','Italic','Underline','Strike','-','Subscript','Superscript'], 
            ['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'], 
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'], 
            ['Link','Unlink','Anchor'], 
            ['Image','Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak'], 
            ['Styles','Format','Font','FontSize'], 
            ['TextColor','BGColor'], 
            ['Maximize','ShowBlocks','-','About', 'pbckcode'],
        ),
        'extraPlugins': 'codesnippet',
        'codeSnippet_theme': 'tomorrow-night-blue',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,"static")

#public static file ,example:jquery.js
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

CKEDITOR_UPLOAD_PATH = "article"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js'

