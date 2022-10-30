from django.contrib import admin

from . import models


class ProjectMemberAdmin(admin.TabularInline):
    model = models.ProjectMember
    autocomplete_fields = ["user"]
    extra = 1  # how many rows to show


@admin.register(models.Project)
class Project(admin.ModelAdmin):
    autocomplete_fields = ["manager"]
    prepopulated_fields = {"slug": ("title",)}

    inlines = (ProjectMemberAdmin,)
