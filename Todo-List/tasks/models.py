from django.db import models


# Create your models here.

class Todo(models.Model):
    doing = 0
    done = 1

    STATUS = ((done, 'In progress'),
              (doing, 'Finished'))

    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1, choices=STATUS)

    def __str__(self):
        return self.title
