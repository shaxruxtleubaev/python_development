from django.db import models


class Project(models.Model):
    title = models.CharField('Заголовок', max_length=30, blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)
    technology = models.CharField('Технология', max_length=30, blank=True, null=True)
    image = models.FilePathField(path='./images')
    date = models.DateTimeField('Время', auto_now_add=True)

    def __str__(self):
        return self.title
