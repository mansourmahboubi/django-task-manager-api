from django.contrib.auth.models import UserManager
from django.db import models


class CustomUserManager(UserManager):
    def login(self, user, token) -> str:
        user.token = token
        user.save()
        return user
