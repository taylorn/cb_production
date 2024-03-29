# Django settings for crimsonbeacon project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

SIDEBAR_URLS = (
    '/articles/',
    '/survey-reports/',
    '/case-studies/',
    '/contributor/',
)

ADMIN_PANEL_URL = 'admin-panel'
ADMIN_LOGIN_URL = 'admin-login'

TWITTER_POSTING_ON = True
LINKEDIN_POSTING_ON = True
FACEBOOK_POSTING_ON = True
PLAXO_POSTING_ON = True

OAUTH_TOKEN = '801628326-PrjyrV4j0Tw8I2puYc8nyUOD6iM1WV7yMdEkd6Nn'
OAUTH_SECRET = 'jXIegVI9wJLDLmP02MO7hK9Z33I7m5KM1j1J1f1Zrc'
TWITTER_TOKEN = 'Y48o4yqkm6zKSIBg72Fw'
TWITTER_SECRET = 'hOlcAri9RyqvI9gCZo380wLLoy0lkWWN4Py2q4LQTY4'
FACEBOOK_ID = '170935919718208'
FACEBOOK_SECRET = '457115335bfcc9efbabd49735f77e2c7'
LINKEDIN_API_KEY = 'i8o78osmcid9'
LINKEDIN_SECRET = '9pk2Ynl4A3HlpAfa'
LINKEDIN_OAUTH_TOKEN = '92c8a025-0114-4203-81cb-7554c36af187'
LINKEDIN_OAUTH_SECRET = '79ada979-8ced-4aca-9b3b-e7b7ce97b7a2'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'taylorn',                      # Or path to database file if using sqlite3.
        'USER': 'taylorn',                      # Not used with sqlite3.
        'PASSWORD': 'freekshow3/',                  # Not used with sqlite3.
        'HOST': 'web347.webfaction.com',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/taylorn/webapps/staticfiles/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'http://www.crimsonbeacon.com/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/taylorn/webapps/cb_django/myproject/static/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$h2=n*mr1zl_w#0vt1ew@(6g@=4j&amp;i8s-+nzwdb=pbt__stjn$'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",

    'myproject.context_processors.assign_sidebar',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'myproject.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'myproject.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/taylorn/webapps/cb_django/myproject/apps/article/templates',
    '/home/taylorn/webapps/cb_django/myproject/apps/case/templates',
    '/home/taylorn/webapps/cb_django/myproject/apps/survey/templates',
    '/home/taylorn/webapps/cb_django/myproject/templates',
    '/home/taylorn/webapps/cb_django/myproject/apps',
    
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
     'django.contrib.admindocs',
    'apps.article',
    'apps.survey',
    'apps.case',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
