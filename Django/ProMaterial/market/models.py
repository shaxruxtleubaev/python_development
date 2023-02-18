from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.utils import timezone
from django.shortcuts import reverse

class Shop(models.Model):

    UZBEKISTAN = 'UZB'
    RUSSIA = 'RU'
    USA = 'US'
    UKRAINE = 'UA'

    countries = (
        (UZBEKISTAN, 'Uzbekitan'), 
        (RUSSIA, 'Russia'),
        (USA, 'United states of America'),
        (UKRAINE, 'Ukraine')
    )

    title = models.CharField(_('Title'), max_length=20, blank=True, null=True)
    country = models.CharField(
        _('Country'),
        max_length=20,
        blank=True,
        null=True,
        choices=countries,
        default=UZBEKISTAN
    )

    date = models.DateTimeField(auto_now_add=timezone.now)
    description = models.TextField(_('Desciption'), blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name=_('category'))
    slug = models.SlugField()

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        verbose_name = _('User')
    )

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('shop_detail', args=[str(self.id)])


class Category(models.Model):
    
    name = models.CharField(_('name'), max_length=50)
    date = models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self):
        return f'{self.name}'

