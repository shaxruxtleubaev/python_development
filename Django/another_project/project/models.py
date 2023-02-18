from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Blog(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    authors = models.ManyToManyField('Authors')
    date = models.DateTimeField(default=date.today)

    def __str__(self):
        return self.name


class Authors(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
