from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (  # type: ignore
        (
            _("Extra"),
            {"fields": ("token",)},
        ),
    )


admin.site.register(User, CustomUserAdmin)
