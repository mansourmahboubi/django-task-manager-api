from django.contrib import admin

from . import models


class TaskAssignee(admin.TabularInline):
    model = models.TaskAssignee
    autocomplete_fields = ["user"]
    extra = 1  # how many rows to show


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):

    inlines = (TaskAssignee,)
