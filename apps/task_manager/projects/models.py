from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import ProjectManager


class Project(models.Model):
    title = models.CharField(max_length=400, null=False, blank=False)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="ProjectMember",
        related_name="members",
    )
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = ProjectManager()

    def __str__(self) -> str:
        return f"{self.id}"


class ProjectMember(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False
    )
    project = models.ForeignKey("Project", on_delete=models.CASCADE, null=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id}"
