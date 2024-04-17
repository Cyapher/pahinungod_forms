from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.homePage, name="home_vol"),
    path("form", views.index, name="vol_index"),
    path("list", views.printVolunteers, name="list"),
    path("add", views.createVolunteer, name="add"),
    path("edit/<int:volunteer_id>", views.updateVolunteer, name="edit"),
    path("delete/<int:volunteer_id>", views.deleteVolunteer, name="del_volunteer"),
    path("<int:volunteer_id>/info", views.view_volunteerInfo, name="viewInfo"),
    path("<int:volunteer_id>/license", views.view_volunteerLicense, name="viewLicense"),
    path("<int:volunteer_id>/insurance", views.view_volunteerInsurance, name="viewInsurance"),
    path("<int:volunteer_id>/student", views.view_volunteerStudent, name="viewStudent"),
    path("search", views.searchFilter, name="search"),
    path("program_list", views.printPrograms, name="programs"),
    path("editProgram/<int:program_id>", views.updateProgram, name="edit_program"),
    path("delProgram/<int:program_id>", views.delProgram, name="del_program"),
    path("addProgram", views.createProgram, name="add_program"),
    path("filterDate", views.searchDateRange, name="filter_date"),
    path("sort", views.sort_data, name="sort"),
    path("filter", views.filterVolunteers, name="filter_vol")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
