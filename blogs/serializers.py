from rest_framework import serializers
from .models import Tag, Blog

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id', 'title', 'image', 'category', 'author', 'author_pic',
                  'published_date', 'reading_time', 'content', 'tags']
