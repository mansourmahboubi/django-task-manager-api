from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from ninja import Router

from apps.accounts.api.schemas import UserNameSchema
from apps.accounts.models import User

from .. import models, services

router = Router()


@router.post("/tasks/{task_id}/assign/")
def assign_tasks(request, task_id, body: UserNameSchema):
    # TODO: more meaning full error
    task = get_object_or_404(models.Task, id=task_id)
    user = get_object_or_404(User, username=body.username)
    services.assign_task(task=task, user=user, assigner=request.auth)
    return 200, {"detail": _("Task assinged.")}
