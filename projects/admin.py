from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_name', 'location', 'project_type', 'project_stage', 'start_date']
    search_fields = ['client_name', 'location', 'project_type', 'project_stage']
    list_filter = ['project_stage', 'location', 'project_type', 'start_date']

admin.site.register(Project, ProjectAdmin)
