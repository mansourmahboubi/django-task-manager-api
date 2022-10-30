from typing import List, Optional

from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from ninja import Router

from apps.accounts.api.schemas import UserNameSchema
from apps.accounts.models import User
from apps.task_manager.projects.models import Project

from .. import models, services
from . import schemas

router = Router()


@router.get("/project/{project_slug}/tasks/", response={200: List[schemas.TaskSchema]})
def tasks_list(request, project_slug, username: Optional[str] = None):
    # TODO: more meaning full error
    project = get_object_or_404(Project, slug=project_slug)
    tasks_list = services.tasks_list(project=project, username=username)
    return tasks_list


@router.post("/tasks/{task_id}/assign/")
def assign_tasks(request, task_id, body: UserNameSchema):
    # TODO: more meaning full error
    task = get_object_or_404(models.Task, id=task_id)
    user = get_object_or_404(User, username=body.username)
    services.assign_task(task=task, user=user)
    return 200, {"detail": _("Task assinged.")}
