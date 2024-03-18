from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list", views.printVolunteers, name="list"),
    path("add", views.createVolunteer, name="add"),
    path("edit/<int:volunteer_id>", views.updateVolunteer, name="edit"),
    path("delete/<int:volunteer_id>", views.deleteVolunteer, name="del_volunteer"),
    path("<int:volunteer_id>/info", views.view_volunteerInfo, name="viewInfo"),
    path("<int:volunteer_id>/license", views.view_volunteerLicense, name="viewLicense"),
    path("<int:volunteer_id>/insurance", views.view_volunteerInsurance, name="viewInsurance"),
    path("<int:volunteer_id>/student", views.view_volunteerStudent, name="viewStudent")
]
