from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
from tasks.models import User

class Note(models.Model):
    title=models.CharField(max_length=50)
    message=models.CharField(max_length=500)
    datetime=models.DateTimeField()
    owner=models.ForeignKey(User,on_delete=CASCADE,related_name="notes")