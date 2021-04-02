from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django import forms
from . import util
from .models import User, task
import datetime

def index(request):
    return render(request,"tasks/index.html")

def add(request):
    if request.method == "POST":
        title=request.POST["title"]
        sdate=request.POST['sdate']
        edate=request.POST['edate']
        stime=request.POST['stime']
        etime=request.POST['etime']
        description=request.POST['description']
        user_id=request.POST['user_id']
        owner=User.objects.get(pk=user_id)
        tsk = task(sdate= sdate,edate= edate,stime= stime,etime= etime,title= title,description= description,owner=owner)
        tsk.save()
        owner.tasks.add(tsk)
        return HttpResponseRedirect(reverse('index'))
    return render(request, "tasks/add.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "tasks/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "tasks/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method == "POST":
        uname = request.POST["username"]
        em = request.POST["email"]
        # Ensure password matches confirmation
        pswd = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if pswd != confirmation:
            return render(request, "tasks/register.html", {
                "message": "Passwords must match."
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(username=uname,password=pswd,email=em)
            user.save()
        except IntegrityError:
            return render(request, "tasks/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "tasks/register.html")

def task_view(request,task_id):
    # temp=User.objects.get(pk=user_id)
    # tsk=task.objects.get(pk=task_id,owner=temp)
    tsk=task.objects.get(pk=task_id)
    return render(request,"tasks/task.html",{
        "task":tsk
    })