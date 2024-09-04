from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = [
            'id', 
            'client_name', 
            'location', 
            'project_type', 
            'builtup_area', 
            'project_stage', 
            'start_date', 
            'end_date', 
            'description', 
            'image',
            'passcode'
        ]
