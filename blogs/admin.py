from django.contrib import admin
from .models import Tag, Blog

class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']

admin.site.register(Tag, TagAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'author', 'published_date']
    search_fields = ['title', 'category', 'author']
    list_filter = ['tags']

admin.site.register(Blog, BlogAdmin)
