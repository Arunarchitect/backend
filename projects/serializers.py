from rest_framework import serializers
from .models import Project, ProjectImage

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image', 'image_name']

class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)  # Read-only

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
            'passcode',
            'images'  # List of 360-degree images
        ]

class ProjectCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListSerializer(child=serializers.DictField(), write_only=True)

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
            'passcode',
            'images'  # List of 360-degree images
        ]

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        project = Project.objects.create(**validated_data)
        for image_data in images_data:
            ProjectImage.objects.create(project=project, **image_data)
        return project

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', [])
        instance.client_name = validated_data.get('client_name', instance.client_name)
        instance.location = validated_data.get('location', instance.location)
        instance.project_type = validated_data.get('project_type', instance.project_type)
        instance.builtup_area = validated_data.get('builtup_area', instance.builtup_area)
        instance.project_stage = validated_data.get('project_stage', instance.project_stage)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.description = validated_data.get('description', instance.description)
        instance.passcode = validated_data.get('passcode', instance.passcode)
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        # Handle images
        existing_images = set(instance.images.values_list('id', flat=True))
        new_images = set()

        for image_data in images_data:
            image_id = image_data.get('id')
            if image_id:
                try:
                    image = ProjectImage.objects.get(id=image_id)
                    image.image = image_data.get('image', image.image)
                    image.image_name = image_data.get('image_name', image.image_name)
                    image.save()
                    new_images.add(image.id)
                except ProjectImage.DoesNotExist:
                    continue
            else:
                ProjectImage.objects.create(project=instance, **image_data)
                new_images.add(image.id)

        # Delete removed images
        for image_id in existing_images - new_images:
            ProjectImage.objects.filter(id=image_id).delete()

        return instance
