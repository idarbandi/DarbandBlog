from pathlib import Path
from .local_settings import * 
from datetime import timedelta
BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # Built-ins
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles", 
    # internal apps 
    "user", # Custome user app
    "blog",
    "blog_api",
    #third party packages
    "rest_framework",
    'corsheaders',
    "rest_framework_simplejwt.token_blacklist",
    'rest_framework_swagger',
]

AUTH_USER_MODEL = 'user.User'


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',  # for localhost (REACT Default)
    'http://127.0.0.1:3000',  # for network
    'http://localhost:8080',  # for localhost (Developlemt)
    'http://192.168.0.50:8080',  # for network (Development)
)

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',  # for localhost (REACT Default)
    'http://192.168.0.50:3000',  # for network
    'http://localhost:8080',  # for localhost (Developlemt)
    'http://192.168.0.50:8080',  # for network (Development)
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    "Authorization",
    "Content-Type",
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]


ROOT_URLCONF = "Backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "Backend.wsgi.application"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_RESFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    
    "AUTH_HEADER_TYPES": ("Bearer", "JWT"),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
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

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"