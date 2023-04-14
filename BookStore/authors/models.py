from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.SmallIntegerField()
    birth_data =  models.DateField()
    bio = models.TextField()

    def __str__(self):
        return self.name