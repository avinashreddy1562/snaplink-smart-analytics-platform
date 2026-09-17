from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Project-owned user model defined before the initial migration."""

    email = models.EmailField("email address", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.username
