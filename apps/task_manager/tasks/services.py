from typing import Optional

from django.utils.translation import gettext_lazy as _

from apps.accounts.models import User
from apps.task_manager.projects.models import Project

from . import models


def tasks_list(*, project: Project, username: Optional[str]):
    # TODO: better query
    tasks = models.Task.objects.filter(project=project)
    if username:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return []
        tasks = tasks.filter(assignees__in=[user])
    return tasks


def assign_task(*, task: models.Task, user: User) -> models.TaskAssignee:
    # Todo: add perm check
    task_assignee_obj = models.TaskAssignee.objects.create(user=user, task=task)
    return task_assignee_obj
