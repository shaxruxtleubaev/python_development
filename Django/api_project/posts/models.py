from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from users.models import CustomUser

class Calendar(models.Model):
	user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	name = models.CharField(max_length=45)

	def __str__(self):
		return str(self.id)

class Event(models.Model):
	calendar_id = models.ForeignKey(Calendar, on_delete=models.CASCADE)
	user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	name = models.CharField(max_length=45)
	location = models.CharField(max_length=45)
	startdate = models.DateField()
	enddate = models.DateField()

	def __str__(self):
		return str(self.id)

class Invitees(models.Model):
	event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
	user_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

"""
class Post(models.Model):
	title = models.CharField(max_length=50)
	body = models.TextField()
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	#author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
"""