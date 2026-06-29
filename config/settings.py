"""Настройки проекта ДДС."""

import os
from pathlib import Path

from dotenv import load_dotenv

# Базовый путь проекта.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# Настройки для локальной разработки.

# Для production SECRET_KEY должен храниться в защищенном окружении.
SECRET_KEY = os.getenv("SECRET_KEY")

# Для production DEBUG должен быть выключен.
DEBUG = os.getenv("DEBUG", "False") == "True"

# Список хостов читается из env, чтобы локальный и Docker-запуск совпадали.
ALLOWED_HOSTS = [
    host.strip() for host in os.getenv("ALLOWED_HOSTS", "").split(",") if host.strip()
]


# Приложения проекта.

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "cashflow",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# База данных.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        # Для Docker SQLite лежит в volume, локально используется db.sqlite3.
        "NAME": os.getenv("SQLITE_NAME", BASE_DIR / "db.sqlite3"),
    }
}


# Валидация паролей.

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
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


# Локализация.

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Asia/Novosibirsk"

USE_I18N = True

USE_TZ = True


# Статические файлы.

STATIC_URL = "static/"
