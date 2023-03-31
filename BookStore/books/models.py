from django.db import models
from authors.models import Author
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published = models.DateField()
    price =   models.DecimalField(max_digits=7, decimal_places=2)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title