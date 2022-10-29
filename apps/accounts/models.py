import binascii
import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    token = models.CharField(
        _("Token"), db_index=True, unique=True, max_length=50, null=True, blank=True
    )
    objects = CustomUserManager()

    @classmethod
    def generate_key(cls) -> str:
        """
        https://gist.github.com/geoffalday/2021517
        Generates auth key
        """
        return binascii.hexlify(os.urandom(24)).decode()
