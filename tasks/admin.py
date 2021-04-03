from django.contrib import admin

from .models import User,task
# Register your models here.
admin.site.register(User)
admin.site.register(task)