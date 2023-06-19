from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'created_at',
        'updated_at',
        'tags',
    ]
    list_filter = [
        'tags',
    ]
    search_fields = [
        'title',
        'author',
    ]
    list_display_links = [
        'title',
        'author',
    ]
    ordering = [
        '-updated_at',
        '-created_at',
        'title',
    ]
    list_per_page = 50

admin.site.register(Post, PostAdmin)