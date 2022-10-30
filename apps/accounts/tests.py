from importlib import reload

import pytest
from django.contrib import auth
from ninja.errors import HttpError

from . import services
from .models import User


class TestSetLogin:
    @pytest.fixture
    def user(self):
        return User(
            first_name="test",
            last_name="test last name",
            email="asdf@email.com",
            username="asdf@email.com",
        )

    def test_sets_successful_login(self, mocker, user):
        input = {"username": "test", "password": "123"}

        mock_authenticate = mocker.patch.object(auth, "authenticate", return_value=user)
        mock_login = mocker.patch.object(User.objects, "login")

        # reload module after mocking
        reload(services)

        token = services.login(**input)

        mock_authenticate.assert_called_once_with(**input)
        mock_login.assert_called_once_with(user, token)

    def test_sets_un_successful_login(self, mocker, user):
        input = {"username": "test", "password": "123"}

        mock_authenticate = mocker.patch.object(auth, "authenticate", return_value=None)
        mock_login = mocker.patch.object(User.objects, "login")

        # reload module after mocking
        reload(services)

        with pytest.raises(HttpError) as error:
            services.login(**input)

        mock_authenticate.assert_called_once_with(**input)
        mock_login.assert_not_called()
