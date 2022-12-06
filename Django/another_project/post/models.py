from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField('Загаловок', max_length=200, blank=True, null=True)
    text = models.TextField()
    createdAt = models.DateTimeField(default=timezone.now)
    pubDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.pubDate = timezone.now()
        self.save()

    def __str__(self):
        return self.title
