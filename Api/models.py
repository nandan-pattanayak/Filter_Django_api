from django.db import models

# Create your models here.

class StudentDetail(models.Model):
	name = models.CharField(max_length=30)
	stream = models.CharField(max_length=30)
	year = models.CharField(max_length=30)
	project = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	phone = models.CharField(max_length=12)
	def __str__(self):
		return self.name