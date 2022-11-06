import pytest
from django.contrib.auth.models import Group
from ninja.errors import HttpError

from apps.accounts.models import User
from apps.task_manager.projects.models import Project

from . import models, services


class TestSetAssignTask:
    @pytest.fixture
    def user(self):
        return User(
            id=5,
            first_name="test",
            last_name="test last name",
            email="asdf@email.com",
            username="asdf@email.com",
        )

    @pytest.fixture
    def assigner(self):
        return User(
            id=1,
            first_name="man",
            last_name="manager",
            email="manager@email.com",
            username="manager@email.com",
        )

    @pytest.fixture
    def task(self, assigner):
        project = Project(title="test", manager=assigner)
        task = models.Task(
            project=project,
            title="title 1",
        )
        return task

    def test_sets_un_authorized_assign(self, mocker, task, user, assigner):

        mock_create = mocker.patch.object(models.TaskAssignee.objects, "create")
        mock_has_perm = mocker.patch.object(user, "has_perm", return_value=False)

        with pytest.raises(HttpError):
            # call with regular user
            services.assign_task(task=task, user=user, assigner=user)

        mock_has_perm.assert_called_once_with("tasks.add_taskassignee")
        mock_create.assert_not_called()

    def test_sets_authorized_assign(self, mocker, task, user, assigner):
        mock_create = mocker.patch.object(models.TaskAssignee.objects, "create")
        mock_has_perm = mocker.patch.object(assigner, "has_perm", return_value=True)

        services.assign_task(task=task, user=user, assigner=assigner)

        mock_has_perm.assert_called_once_with("tasks.add_taskassignee")
        mock_create.assert_called_once_with(task=task, user=user)
