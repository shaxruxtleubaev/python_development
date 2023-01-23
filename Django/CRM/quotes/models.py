from django.db import models
from django.contrib.auth.models import User

class Quote(models.Model):

	STATUS_CHOICES = (
		('NEW', 'New site'),
		('EX', 'Existing site'),
	)

	PRIORITY_CHOICES = (
		('U', 'Urgent - 1 week or less'),
		('N', 'Normal - 2 to 4 weeks'),
		('L', 'Low - Still researching'),
	)


	name = models.CharField(max_length=100, blank=True, null=True)
	position = models.CharField(max_length=60, blank=True, null=True)
	company = models.CharField(max_length=60, blank=True, null=True)
	address = models.CharField(max_length=150, blank=True, null=True)
	phone = models.CharField(max_length=60, blank=True, null=True)
	email = models.EmailField()
	web = models.URLField(blank=True)
	description = models.TextField()
	sitestatus = models.CharField(max_length=60, choices=STATUS_CHOICES)
	priority = models.CharField(max_length=60, choices=PRIORITY_CHOICES)
	jobfile = models.FileField(upload_to='uploads/', blank=True)
	submitted = models.DateField(auto_now_add=True)
	quotedate = models.DateField(blank=True, null=True)
	quoteprice = models.DecimalField(decimal_places=2, max_digits=7, blank=True, default=0)
	user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

