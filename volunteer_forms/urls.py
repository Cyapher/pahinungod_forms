from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list", views.printVolunteers, name="list"),
    path("add", views.createVolunteer, name="add")
]
