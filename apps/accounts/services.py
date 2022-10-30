from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from ninja.errors import HttpError

from .models import User


def login(*, username: str, password: str):
    user = authenticate(username=username, password=password)
    if user is None:
        raise HttpError(401, _("Password is not correct or user not exists."))
    new_token = User.generate_key()
    User.objects.login(user, new_token)
    return new_token


def signup(user_data) -> User:
    password = user_data.pop("password")
    user = User(**user_data)
    user.set_password(password)
    user.save()
    return user
