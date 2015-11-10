from django.db import models

# Create your models here.

class User(models.Model):
	full_name = models.CharField(max_length=120, blank=True, null=True)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=50)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.full_name

class Faq(models.Model):
	question = models.CharField(max_length=200)
	answer = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.question

class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	quantity = models.IntegerField()
	description = models.TextField()
	picture = models.FileField(upload_to='img', max_length=100)

	def __str__(self):
		return self.name

class Project(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	location = models. CharField(max_length=100)
	picture	= models.FileField(upload_to='img', max_length=100)

	def __str__(self):
		return self.name


class Cart(models.Model):
	user = models.ForeignKey(User)
	project = models.ForeignKey(Project, default=1)
	product = models.ForeignKey(Product)
	quantity = models.IntegerField(default=0)

	def __str__(self):
		return str(self.quantity)
