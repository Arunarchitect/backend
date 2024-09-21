from rest_framework import serializers
from .models import Project, ProjectImage

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image', 'image_name']

class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)  # Read-only for images

    class Meta:
        model = Project
        fields = [
            'id', 
            'client_name', 
            'location', 
            'project_type', 
            'builtup_area', 
            'start_date', 
            'end_date', 
            'description', 
            'image', 
            'passcode',
            'images',
            'lod100_status',
            'lod200_status',
            'lod300_status',
            'lod400_status',
            'lod500_status',
        ]

class ProjectCreateSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, write_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 
            'client_name', 
            'location', 
            'project_type', 
            'builtup_area', 
            'start_date', 
            'end_date', 
            'description', 
            'image', 
            'passcode',
            'images',
            'lod100_status',
            'lod200_status',
            'lod300_status',
            'lod400_status',
            'lod500_status',
        ]

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        project = Project.objects.create(**validated_data)

        for image_data in images_data:
            ProjectImage.objects.create(project=project, **image_data)

        return project

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', [])

        # Update Project fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
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
                new_image = ProjectImage.objects.create(project=instance, **image_data)
                new_images.add(new_image.id)

        # Delete removed images
        for image_id in existing_images - new_images:
            ProjectImage.objects.filter(id=image_id).delete()

        return instance
