import os
import dj_database_url

from pathlib import Path
from urllib.parse import urlparse, parse_qs

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    "anymail",
    "fontawesomefree",
    "pages",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.styleguide",
    "wagtail.contrib.table_block",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sitemaps",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.legacy.sitemiddleware.SiteMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

sentry_dsn = os.environ.get("SENTRY_DSN", "")
if sentry_dsn:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    def ignore_disallowedhost(event, hint):
        if event.get("logger", None) == "django.security.DisallowedHost":
            return None
        return event

    sentry_sdk.init(
        dsn=sentry_dsn,
        before_send=ignore_disallowedhost,
        integrations=[DjangoIntegration()],
        release=os.environ.get("GIT_COMMIT", "develop"),
        environment=os.environ.get("STAGE", "local"),
        traces_sample_rate=0.2,
    )

ROOT_URLCONF = "urls"

SECRET_KEY = os.environ.get("SECRET_KEY", "<a string of random characters>")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "False") == "True"

DIVIO_DOMAIN = os.environ.get("DOMAIN", "")
DIVIO_DOMAIN_ALIASES = [
    d.strip() for d in os.environ.get("DOMAIN_ALIASES", "").split(",") if d.strip()
]
DIVIO_DOMAIN_REDIRECTS = [
    d.strip() for d in os.environ.get("DOMAIN_REDIRECTS", "").split(",") if d.strip()
]

ALLOWED_HOSTS = [DIVIO_DOMAIN] + DIVIO_DOMAIN_ALIASES + DIVIO_DOMAIN_REDIRECTS

CSRF_TRUSTED_ORIGINS = [
    os.environ.get("CSRF_TRUSTED_ORIGINS", default="https://fourfridays.com")
]

# Redirect to HTTPS by default disabled, unless explicitly enabled
SECURE_SSL_REDIRECT = os.environ.get("SECURE_SSL_REDIRECT") == "True"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
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

# Authentication Backends
AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

# Search Backends
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

WSGI_APPLICATION = "wsgi.application"

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite://:memory:")

DATABASES = {
    "default": dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=0,
        conn_health_checks=False,
    )
}

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

LANGUAGE_CODE = "en-us"
USE_I18N = True
USE_TZ = True
TIME_ZONE = "UTC"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = ["static"]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATIC_URL = "/static/"

# read the setting value from the environment variable
DEFAULT_STORAGE_DSN = os.environ.get(
    "DEFAULT_STORAGE_DSN",
    "file:///data/media/?url=%2Fmedia%2F"
)

def parse_s3_url(s3_url):
    parsed_url = urlparse(s3_url)

    # Extract credentials (if present)
    if '@' in parsed_url.netloc:
        auth, netloc = parsed_url.netloc.split('@')
        access_key, secret_key = auth.split(':')
    else:
        access_key = secret_key = None
        netloc = parsed_url.netloc

    # Extract bucket and domain
    domain_parts = netloc.split('.s3.amazonaws.com')
    bucket_name = domain_parts[0] if len(domain_parts) > 1 else None
    domain = "s3.amazonaws.com" if len(domain_parts) > 1 else netloc

    # Extract query parameters
    query_params = parse_qs(parsed_url.query)

    return {
        "access_key": access_key,
        "secret_key": secret_key,
        "bucket_name": bucket_name,
        "domain": domain,
        "query_params": query_params
    }

s3_url = DEFAULT_STORAGE_DSN
parsed_result = parse_s3_url(s3_url)

if parsed_result["access_key"] and parsed_result["secret_key"]:
    STORAGE_BACKEND = "storages.backends.s3boto3.S3Boto3Storage"
    AWS_S3_ACCESS_KEY_ID = parsed_result.get("access_key")
    AWS_S3_SECRET_ACCESS_KEY = parsed_result.get("secret_key")
    AWS_STORAGE_BUCKET_NAME = parsed_result.get("bucket_name")
    AWS_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME
    AWS_DEFAULT_ACL = "public-read"
    AWS_S3_FILE_OVERWRITE = True
    AWS_QUERYSTRING_AUTH = False
    AWS_IS_GZIPPED = True
else:
    STORAGE_BACKEND = "django.core.files.storage.FileSystemStorage"
    # only required for local file storage and serving, in development
    MEDIA_URL = "media/"
    MEDIA_ROOT = os.path.join("/data/media/")

STORAGES = {
    "default": {
        "BACKEND": STORAGE_BACKEND,
    },
    # ManifestStaticFilesStorage is recommended in production, to prevent
    # outdated JavaScript / CSS assets being served from cache
    # See https://docs.djangoproject.com/en/5.1/ref/contrib/staticfiles/#manifeststaticfilesstorage
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

WAGTAIL_SITE_NAME = "fourfridays"
WAGTAILADMIN_BASE_URL = "https://fourfridays.com/"

# DJANGO ANYMAIL
ANYMAIL = {
    "MAILGUN_API_KEY": os.environ.get("MAILGUN_API_KEY", default=""),
    "MAILGUN_SENDER_DOMAIN": os.environ.get("MAILGUN_SENDER_DOMAIN", default=""),
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", default="")
SERVER_EMAIL = os.environ.get("SERVER_EMAIL", default="")

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
PREPEND_WWW = os.environ.get("PREPEND_WWW", default=False)
SITE_ID = 1

# Make low-quality but small images
WAGTAILIMAGES_JPEG_QUALITY = 70
WAGTAILIMAGES_WEBP_QUALITY = 75
WAGTAIL_ENABLE_WHATS_NEW_BANNER = False

# Logging configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "info.log"),
            "formatter": "verbose",
        },
        "sentry": {
            "level": "ERROR",  # Capture errors and above to Sentry
            "class": "sentry_sdk.integrations.logging.EventHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file", "sentry"],
            "level": "INFO",
            "propagate": True,
        },
    },
}

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10_000
