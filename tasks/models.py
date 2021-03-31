from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# Create your models here.

class task(models.Model):
    sdate=models.DateField()
    stime=models.TimeField()
    edate=models.DateField()
    etime=models.TimeField()
    title=models.CharField()
    description=models.CharField()

class User(AbstractUser):
    tasks=models.ForeignKey(task,on_delete=CASCADE)

