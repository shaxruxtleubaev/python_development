from django.db import models

class Two(models.Model):
    title = models.CharField(max_length=27, blank=True, null=True)
    content = models.TextField()

    def __str__(self):

        return f'{self.title}'