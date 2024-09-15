from django.contrib import admin
from .models import Project, ProjectImage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('image_name', 'project', 'image')
