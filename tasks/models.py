from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# Create your models here.

class task(models.Model):
    sdate=models.DateField()
    stime=models.TimeField()
    edate=models.DateField()
    etime=models.TimeField()
    title=models.CharField(max_length=64)
    description=models.CharField(max_length=400)

class User(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField(blank=True)
    tasks=models.ForeignKey(task,on_delete=CASCADE)

