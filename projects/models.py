from django.db import models

# Create your models here.
class Project(models.Model):
    client_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    project_type = models.CharField(max_length=255)
    builtup_area = models.DecimalField(max_digits=10, decimal_places=2)
    project_stage = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # Optional if the project is ongoing
    description = models.TextField(blank=True)  # Optional project description
    image = models.ImageField(
        default="images/projects/default.png",
        upload_to="images/projects",
        max_length=255,
        blank=False,
    )

    def __str__(self):
        return f"{self.client_name} - {self.project_type}"

    class Meta:
        verbose_name_plural = 'Projects'
        ordering = ['id']