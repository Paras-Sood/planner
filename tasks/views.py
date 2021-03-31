from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from django import forms
from . import util
from .models import User

# class NewTaskForm(forms.Form):
#     name=forms.CharField(label="name")

# Create your views here.
# def index(request):
#     content=[]
#     entries=util.list_entries()
#     for entry in entries:
#         content.append(util.get_entry(entry))
#         print(util.get_entry(entry))
#     return render(request, "tasks/index.html",{
#         "tasks":util.list_entries(),
#         "content":content
#     })

def index(request):
    return render(request, "planner/index.html",{
        "tasks":User.tasks.all()
    })

def add(request):
    if request.method == "POST":
        title=request.POST["title"]
        sdate=request.POST['sdate']
        edate=request.POST['edate']
        stime=request.POST['stime']
        etime=request.POST['etime']
        description=request.POST['description']
        User.task.add()
        return render(request,"tasks/index.html",{
            "title":title,
        })
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

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")