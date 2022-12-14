from typing import List, Optional

from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from ninja import Router

from apps.task_manager.tasks import services
from apps.task_manager.tasks.api import schemas

from ..models import Project

router = Router()


@router.get("/project/{project_slug}/tasks/", response={200: List[schemas.TaskSchema]})
def tasks_list(request, project_slug, username: Optional[str] = None):
    # TODO: more meaning full error
    project = get_object_or_404(Project, slug=project_slug)
    tasks_list = services.tasks_list(project=project, username=username)
    # TODO: pagination
    return tasks_list
