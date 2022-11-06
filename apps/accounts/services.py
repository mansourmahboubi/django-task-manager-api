from typing import Any, Dict, cast

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from ninja.errors import HttpError

from .models import User


def login(*, username: str, password: str):
    user = authenticate(username=username, password=password)
    if user is None:
        raise HttpError(401, _("Password is not correct or user not exists."))
    new_token = User.generate_key()
    User.objects.login(cast(User, user), new_token)
    return new_token


def signup(user_data: "Dict[str, Any]") -> User:
    username = user_data.pop("username")
    password = user_data.pop("password")
    email = user_data.pop("email")
    user = User.objects.create_user(username, email, password, **user_data)
    return user
