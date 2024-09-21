from django.contrib import admin
from .models import Project, ProjectImage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'project_type', 'start_date', 'end_date', 'builtup_area')
    search_fields = ('client_name', 'project_type')
    list_filter = ('start_date', 'end_date', 'client_name')

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('image_name', 'project', 'image')
    list_filter = ('project',)
