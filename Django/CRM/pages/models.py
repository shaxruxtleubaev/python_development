from django.db import models
from ckeditor import fields

class Page(models.Model):

	title = models.CharField('Название', max_length=100)
	permalink = models.CharField('Постоянная ссылка', max_length=12, unique=True)
	update_date = models.DateTimeField('Последняя публикация', auto_now_add=True)
	body_text = fields.RichTextField('Контент', blank=True, null=True)

	class Meta:

		verbose_name_plural = 'Страницы'
		verbose_name = 'Страница'

	def __str__(self):
		return self.title
