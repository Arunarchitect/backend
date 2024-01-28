from django.db import models
from tinymce.models import HTMLField


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Tags'
        ordering = ['id']


class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(
        default="images/blogs/doc.png",
        upload_to="images/blogs",
        max_length=255,
        blank=False,
    )
    category = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    author_pic = models.ImageField(
        default="images/blogs/doc.png",
        upload_to="images/blogs",
        max_length=255,
        blank=False,
    )
    published_date = models.DateField()
    reading_time = models.CharField(max_length=20)
    content = HTMLField(blank=False, default='')
    tags = models.CharField(max_length=20, default='BIM')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Blogsss'
        ordering = ['id']
