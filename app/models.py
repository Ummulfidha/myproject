from django.db import models

# Create your models here.
#Admin

class adminloginmodel(models.Model):
    email = models.EmailField(max_length=50)
    pwd = models.CharField(max_length=20)

class addtrainermodel(models.Model):
    tname = models.CharField(max_length=20)
    tage = models.IntegerField()
    tphone = models.IntegerField()
    tgender = models.CharField(max_length=10)
    temail = models.EmailField(max_length=25)
    tadm = models.CharField(max_length=34, default='test')

#trainer

class trainerloginmodel(models.Model):
    email = models.EmailField(max_length=50)
    pwd = models.CharField(max_length=20)

