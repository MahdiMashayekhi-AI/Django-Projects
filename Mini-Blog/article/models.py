from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from autoslug import AutoSlugField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse("article:post_detail", args=[str(self.slug)])
    
    def increment_view(self):
        self.views += 1
        self.save()
        

    def __str__(self):
        return self.title
    