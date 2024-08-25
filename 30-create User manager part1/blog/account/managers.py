from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("the username field must be set")
        if not email:
            raise ValueError("the email field must be set")
        if not password:
            raise ValueError("the password field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username , email=email, **extra_fields)
        user.set_password(password)

    def create_superuser:
        pass
