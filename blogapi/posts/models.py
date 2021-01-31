from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import truncatechars

class CustomUser(AbstractUser):
	pass

class Post(models.Model):
	author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	entry = models.TextField()

	@property
	def Entry(self):
		return truncatechars(self.entry, 50)
	

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
		
		
# Create your models here.
