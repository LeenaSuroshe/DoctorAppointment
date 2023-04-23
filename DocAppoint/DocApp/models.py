from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    contact=models.CharField(max_length=10)
    spcl=models.CharField(max_length=50)
    ava=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    
class Appointment(models.Model):
    docname=models.CharField(max_length=100)
    docemail=models.EmailField()
    patientname=models.CharField(max_length=100)
    patientemail=models.EmailField()
    appointdate=models.DateField()
    appointtime=models.TextField()
    symptoms=models.CharField(max_length=100)
    status=models.CharField(max_length=100,null=True)
    user=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.patientname+" you have appointment with "+self.docname
    
class Bill(models.Model):
    patientname=models.CharField(max_length=50)
    patientemail=models.EmailField()
    docname=models.CharField(max_length=50)
    docemail=models.EmailField()
    bill=models.TextField(max_length=100)
    med=models.CharField(max_length=1000)
    date=models.DateField(auto_now=True)
    user=models.CharField(max_length=100,null=True)


# class Feedback(models.Model):
#     name=models.CharField(max_length=50)
#     email=models.EmailField()
#     contact=models.CharField(max_length=10)
#     fdb=models.CharField(max_length=1000)