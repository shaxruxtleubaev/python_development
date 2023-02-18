from django.db import models

class Food(models.Model):

    title = models.CharField(max_length=20, blank=True, null=True)
    content = models.TextField()

    def __str__(self):

        return f'{self.title}'