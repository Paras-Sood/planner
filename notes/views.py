from django.forms.widgets import Textarea
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime
from django import forms
from django.urls.base import reverse
from .models import User,Note


class NewNote(forms.Form):
    title=forms.CharField(label="Title",max_length=50,)
    message=forms.CharField(label="Note",widget=Textarea())
    

def index(request):
    return render(request,"notes/index.html")

def addNote(request):
    if request.method == "POST":
        form=NewNote(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            note=form.cleaned_data['message']
            user_id=request.POST['user_id']
            user=User.objects.get(pk=user_id)
            temp=Note(title=title,message=note,datetime=datetime.datetime.now(),owner=user)
            temp.save()
            user.notes.add(temp)
            return HttpResponseRedirect(reverse('notes:index'))
        else:
            return render(request,"notes/add.html",{
                "form":form
            })
    return render(request,"notes/add.html",{
        "form":NewNote()
    })