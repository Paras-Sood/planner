from django.urls import path

from . import views

app_name="notes"

urlpatterns=[
    path('',views.index,name="index"),
    path('addNote/',views.addNote,name="addNote"),
]