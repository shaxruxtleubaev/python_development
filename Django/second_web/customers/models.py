from django.db import models
from datetime import date
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Blog(models.Model):
	name = models.CharField(max_length=100)
	tagline = models.TextField()

	def __str__(self):
		return f'{self.name} - {self.tagline[:5]}...'

	class Meta:
		verbose_name_plural = _('Blog')

class Author(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = _('Author')

class Entry(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	headline = models.CharField(max_length=250)
	body_text = models.TextField()
	pub_date = models.DateField()
	mod_date = models.DateField(default=date.today)
	authors = models.ManyToManyField(Author)
	number_of_comments = models.IntegerField(default=0)
	number_of_pingbacks = models.IntegerField(default=0)
	rating = models.IntegerField(default=5)

	def __str__(self):
		return '%s' % (self.headline)	

	class Meta:
		verbose_name_plural = _('Entry')

class Quest(models.Model):

	name = models.CharField(max_length=50)
	content = models.TextField()
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.name