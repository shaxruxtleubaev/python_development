from django.db import models


class Listings(models.Model):
    title = models.CharField('Заголовок', max_length=75, blank=True, null=True)
    price = models.FloatField('Цена', default=0)
    num_bedrooms = models.IntegerField('Комната')
    num_bathrooms = models.IntegerField('Ванная')
    square_footage = models.IntegerField('Площадь')
    adress = models.CharField('Адрес', max_length=100)

    image = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Список комнат'
        verbose_name_plural = 'Списки'
        ordering = ('-price',)
