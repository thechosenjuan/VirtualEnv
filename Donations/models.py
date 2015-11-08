from django.db import models

# Create your models here.

class User(models.Model):
	full_name = models.CharField(max_length=120, blank=True, null=True)
	email = models.EmailField()
	password = models.CharField(max_length=50)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self
