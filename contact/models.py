from django.db import models

# Create your models here.


class ContactUs(models.Model):
	first_name = models.CharField(max_length=9999)
	last_name = models.CharField(max_length=9999)
	email = models.EmailField(max_length=999)
	details = models.TextField()

	def __str__(self):
		return self.first_name + " " + last_name