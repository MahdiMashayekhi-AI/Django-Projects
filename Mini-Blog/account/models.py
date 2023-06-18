import os
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from PIL import Image


class Account(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='account_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='account_user_permissions', blank=True)
    followers = models.PositiveIntegerField(default=0)
    followings = models.PositiveIntegerField(default=0)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='avatars', blank=True, null=True)

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)

            max_size = (800, 800)
            if img.width > max_size[0] or img.height > max_size[1]:
                output_size = max_size
                img.thumbnail(output_size)
                img.save(self.image.path)

            max_size_bytes = 2 * 1024 * 1024
            if os.path.getsize(self.image.path) > max_size_bytes:
                self.image.delete()
                self.image = None
                self.save()

    def __str__(self):
        return self.username


class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='user_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_user_permissions', blank=True)
