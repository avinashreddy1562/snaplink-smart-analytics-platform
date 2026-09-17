"""Safe, SQLite-only settings used exclusively by the automated test suite."""

import os

os.environ.setdefault("DJANGO_SECRET_KEY", "snaplink-test-only-secret-not-for-production")

from .settings import *

DEBUG = False
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
