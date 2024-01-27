from django.db import models
from tinymce.models import HTMLField
import os


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255, blank=False)
    subtitle = models.CharField(max_length=255, blank=False)
    content = HTMLField(blank=False, default='')
    image = models.ImageField(default = 'images/blog/doc.png',upload_to = 'images/blog', max_length = 255,blank=False)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Blog'
        ordering = ['title']

    def delete(self, *args, **kwargs):
        # Delete the associated image file
        if self.image.name != 'images/blog/doc.png':
            try:
                os.remove(self.image.path)
            except FileNotFoundError:
                pass

        super().delete(*args, **kwargs)


