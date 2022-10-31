from django.contrib.auth.models import UserManager

from . import models


class CustomUserManager(UserManager):
    def login(self, user: "models.User", token: str) -> "models.User":
        # TODO: update login_time
        user.token = token
        user.save()
        return user
