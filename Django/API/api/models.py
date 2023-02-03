from django.db import models

class Students(models.Model):

    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    roll_number = models.IntegerField(default=0)
    mobile = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.first_name

class Teacher(models.Model):
    student = models.ManyToManyField(Students)

    def __str__(self):
        return f'{self.student}'