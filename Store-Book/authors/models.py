from datetime import date
from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    birthDate =  models.DateField()
    bio = models.TextField()
    image = models.ImageField(upload_to='authors/', default='authors/default.jpg')

    def age(self):
        today = date.today()
        age = today.year - self.birthDate.year
        if today < self.birthDate.replace(year=today.year):
            age -= 1
        return age
        

    def __str__(self):
        return self.name