from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Article(models.Model):

    name = models.CharField(_('name'), max_length=100)
    content = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('article_detail', args=[str(self.id)])
        return reverse('article_detail', kwargs={"slug": self.slug})


