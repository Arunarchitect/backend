from django.db import models
import os

class Project(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    client_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    project_type = models.CharField(max_length=255)
    builtup_area = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # Optional for ongoing projects
    description = models.TextField(blank=True)  # Optional project description
    image = models.ImageField(
        default="images/projects/default.png",
        upload_to="images/projects",
        blank=False,
    )
    passcode = models.IntegerField(default=1234)  # Default passcode

    # LOD fields with dropdown for status
    lod100_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='not_started')
    lod200_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='not_started')
    lod300_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='not_started')
    lod400_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='not_started')
    lod500_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='not_started')

    def __str__(self):
        return f"{self.client_name} - {self.project_type}"

    class Meta:
        verbose_name_plural = 'Projects'
        ordering = ['id']

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/projects/360degree")
    image_name = models.CharField(max_length=255)

    def __str__(self):
        return self.image_name

    def delete(self, *args, **kwargs):
        # Delete the file from the filesystem
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)  # Call the superclass's delete method
