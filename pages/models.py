from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    full_name = models.CharField(max_length=1000)
    designation = models.CharField(max_length=1000)
    desc = models.TextField()
    img = models.ImageField(upload_to='employees/img/')

    def __str__(self):
        return self.full_name + " " + self.designation

class Job(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=10000)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=200)
    creation_date = models.DateField()
 
    def __str__ (self):
        return self.title

class Application(models.Model):
    company = models.CharField(max_length=200, default="")
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant_email = models.EmailField(max_length = 254)
    applicant_name = models.CharField(max_length=200)
    applicant_phone = models.CharField(max_length=200)
    resume = models.FileField(upload_to="")
    apply_date = models.DateField()
 
    def __str__ (self):
        return str(self.applicant_name)