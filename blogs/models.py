from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


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
    author_pic = models.URLField()
    published_date = models.DateField()
    reading_time = models.CharField(max_length=20)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
