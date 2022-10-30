from typing import List, Optional

from django.shortcuts import get_object_or_404
from ninja import Router

from apps.task_manager.projects.models import Project

from .. import services
from . import schemas

router = Router()


@router.get("/project/{project_slug}/tasks/", response={200: List[schemas.TaskSchema]})
def tasks_list(request, project_slug, username: Optional[str] = None):
    # TODO: more meaning full error
    project = get_object_or_404(Project, slug=project_slug)
    tasks_list = services.tasks_list(project=project, username=username)
    return tasks_list
