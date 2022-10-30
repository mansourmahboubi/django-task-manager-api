from typing import Optional

from django.utils.translation import gettext_lazy as _

from apps.accounts.models import User
from apps.task_manager.projects.models import Project

from .models import Task


def tasks_list(*, project: Project, username: Optional[str]):
    # TODO: better query
    tasks = Task.objects.filter(project=project)
    if username:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return []
        tasks = tasks.filter(assignees__in=[user])
    return tasks
