from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField

# Create your models here.

class User(AbstractUser):
    pass

# class User(models.Model):
#     username=models.CharField(max_length=20,unique=True)
#     password=models.CharField(max_length=20)
#     email=models.EmailField()

#     def create_user(self, username,password,email):
#         self.username=username
#         self.password=password
#         self.email=email
#         return self
    # pass

class task(models.Model):
    sdate=models.DateField()
    stime=models.TimeField()
    edate=models.DateField()
    etime=models.TimeField()
    title=models.CharField(max_length=64)
    description=models.CharField(max_length=400)
    # username=models.CharField(max_length=20)
    # password=models.CharField(max_length=20)
    owner=models.ForeignKey(User,on_delete=CASCADE,related_name="tasks")

    def create_task(self,sdate,edate,stime,etime,title,des):
        self.sdate=sdate
        self.edate=edate
        self.stime=stime
        self.etime=etime
        self.title=title
        self.description=des
        return self
    # username=models.CharField(max_length=20)
    # password=models.CharField(max_length=20)
    # email=models.EmailField(blank=True)
    # tasks = models.ManyToManyField(task, blank=True)
