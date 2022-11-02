# Generated by Django 4.1.2 on 2022-11-01 21:16

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.sql import emit_post_migrate_signal
from django.db import migrations
from django.db.models import Q


def pm_forwards_func(apps, schema_editor):
    """
    Add project-manager perms
    """
    # since create signals works with `post_migrate` we need to create them manually
    emit_post_migrate_signal(1, False, "default")

    TaskAssignee = apps.get_model("tasks", "TaskAssignee")
    Task = apps.get_model("tasks", "Task")
    Group = apps.get_model("auth", "Group")
    db_alias = schema_editor.connection.alias

    t_content_types = ContentType.objects.get_for_model(Task)
    ta_content_types = ContentType.objects.get_for_model(TaskAssignee)

    permissions = Permission.objects.using(db_alias).filter(
        Q(content_type=t_content_types) | Q(content_type=ta_content_types)
    )

    project_manger = Group.objects.using(db_alias).get(name="Project Manager")
    project_manger.permissions.add(*permissions.values_list("pk", flat=True))


def pm_reverse_func(apps, schema_editor):
    """
    Remove project-manager perms
    """
    TaskAssignee = apps.get_model("tasks", "TaskAssignee")
    Task = apps.get_model("tasks", "Task")
    Group = apps.get_model("auth", "Group")
    db_alias = schema_editor.connection.alias

    ta_content_type = ContentType.objects.get_for_model(TaskAssignee)
    task_content_type = ContentType.objects.get_for_model(Task)
    permissions = Permission.objects.using(db_alias).filter(
        Q(content_type=ta_content_type) | Q(content_type=task_content_type)
    )
    project_manger = Group.objects.using(db_alias).get(name="Project Manager")
    project_manger.permissions.remove(*permissions.values_list("pk", flat=True))


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "__first__"),
        ("accounts", "0004_auto_20221101_1551"),
        ("tasks", "0003_alter_task_project"),
    ]

    operations = [
        migrations.RunPython(pm_forwards_func, pm_reverse_func),
    ]