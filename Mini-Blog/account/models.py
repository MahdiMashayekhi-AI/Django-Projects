from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe


class Account(AbstractUser):
    groups = models.ManyToManyField(
        Group, related_name='account_groups', blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name='account_user_permissions', blank=True)
    followers = models.PositiveIntegerField(default=0)
    followings = models.PositiveIntegerField(default=0)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='account_images/', blank=True, null=True)

    def increment_followers(self):
        self.followers += 1
        self.save()

    def decrement_followers(self):
        self.followers -= 1
        self.save()

    def increment_followings(self):
        self.followings += 1
        self.save()

    def decrement_followings(self):
        self.followings -= 1
        self.save()

    def display_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        else:
            return '-'

    display_image.short_description = 'Image'

    def __str__(self):
        return self.username


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group, related_name='user_groups', blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name='user_user_permissions', blank=True)
