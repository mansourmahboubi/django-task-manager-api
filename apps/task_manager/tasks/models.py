from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import TaskManager


class Task(models.Model):
    title = models.CharField(max_length=400, default="")
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="TaskAssignee",
        related_name="assignees",
    )
    project = models.ForeignKey(
        "projects.Project", on_delete=models.CASCADE, related_name="task", null=False
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = TaskManager()

    def __str__(self) -> str:
        return f"{self.id}"


class TaskAssignee(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False
    )
    task = models.ForeignKey("Task", on_delete=models.CASCADE, null=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id}"
