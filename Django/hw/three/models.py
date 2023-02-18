from django.db import models

class Three(models.Model):
    title = models.CharField(max_length=25, blank=True, null=True)
    content = models.TextField()

    def __str__(self):

        return f'{self.title}'
