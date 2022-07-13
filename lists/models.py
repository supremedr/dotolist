from cProfile import label
from datetime import datetime
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lista(models.Model):
    title = models.CharField(max_length = 50,)
    author = models.ForeignKey(User, editable = False, on_delete = models.CASCADE)
    slug = models.CharField(max_length = 500, editable = False)

    def __str__(self):
        return self.title


class Task(models.Model):
    lista = models.ForeignKey(Lista, editable=False, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50,)
    details = models.CharField(max_length = 500,)
    periority = models.IntegerField(choices=[(1, 'low'),(2,'medium'),(3,'high')], default=2)
    timing = models.DateTimeField(default = now )
    done = models.BooleanField(default = False)

    def __str__(self):
        return self.title
