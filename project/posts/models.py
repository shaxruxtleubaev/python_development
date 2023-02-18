from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Calendar(models.Model):
    cid = models.ForeignKey(User, on_delete=models.CASCADE)

class Event(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    cid = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    startdate = models.DateField(auto_now_add=True)
    enddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Invitees(models.Model):
    eid = models.ForeignKey(Event, on_delete=models.CASCADE)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
