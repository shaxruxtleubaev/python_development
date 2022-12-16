from django.db import models
from django.utils import timezone

class Shop(models.Model):

    name = models.CharField('Имя', max_length=200, blank=True, null=True)
    body = models.TextField('Тело',blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    stock = models.BooleanField('Сток')
    color = models.CharField('Цвет', max_length=200, blank=True, null=True)
    author = models.CharField('Автор', max_length=200,  blank=True, null=True)
    image = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date',)
