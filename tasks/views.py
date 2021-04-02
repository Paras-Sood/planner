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
    # pass
    if request.method == "POST":
        title=request.POST["title"]
        sdate=request.POST['sdate']
        edate=request.POST['edate']
        stime=request.POST['stime']
        etime=request.POST['etime']
        description=request.POST['description']
        user_id=request.POST['user_id']
        owner=User.objects.get(pk=user_id)
        # User.task.add()
        # ntask=task.objects.create()
        tsk = task(sdate= sdate,edate= edate,stime= stime,etime= etime,title= title,description= description,owner=owner)
        # print(f"Task {tsk}")
        tsk.save()
        owner.tasks.add(tsk)
        return HttpResponseRedirect(reverse('index'))
        # form=NewTaskForm(request.POST)
        # if form.is_valid():
        #     name=form.cleaned_data["name"]
        #     start=request.POST["start"]
        #     end=request.POST["end"]
        #     content= start + " ------------------------------------- " + end
        #     print(content)
        #     util.save_entry(name,content)
        #     return HttpResponseRedirect(reverse(index))
    return render(request, "tasks/add.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # print(f"User = {user}")
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
        # print("Got")
        # Ensure password matches confirmation
        pswd = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if pswd != confirmation:
            return render(request, "tasks/register.html", {
                "message": "Passwords must match."
            })
        # print("Try")

        # Attempt to create new user
        try:
            # user = User.objects.create(username, email, password)
            user = User.objects.create_user(username=uname,password=pswd,email=em)
            user.save()
            # print(f"Saved {user}")
            # test = authenticate(request, username=uname, password=pswd)
            # print(f"User = {test}")
        except IntegrityError:
            return render(request, "tasks/register.html", {
                "message": "Username already taken."
            })
        # user = User(username=username,email=email,password=password)
        # user.save()
        # print(f"After {user.username}")
        # return HttpResponseRedirect(reverse("login"))
        login(request, user)
        # print("Login")
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "tasks/register.html")

def task_view(request,task_id):
    tsk=task.objects.get(pk=task_id)
    return render(request,"tasks/task.html",{
        "task":tsk
    })