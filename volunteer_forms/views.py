from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from volunteer_forms.models import Volunteer
from .forms import VolunteerForm, InsuranceForm, StudentForm, LicenseForm

def index(request):
    return render(request, "form_pg1.html", 
                  {'v_form' : VolunteerForm(), 
                   'i_form' : InsuranceForm(), 
                   'li_form' : LicenseForm(), 
                   's_form' : StudentForm()
                   })

def createVolunteer(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("list"))
        else:
            return render(request, "form_pg1.html", {"form" : form})
        
def createVolunteer(request):
    if request.method == "POST":
        v_form = VolunteerForm(request.POST, prefix='v_form')
        i_form = InsuranceForm(request.POST, prefix='i_form')
        li_form = LicenseForm(request.POST, prefix='li_form')
        s_form = StudentForm(request.POST, prefix='s_form')

def printVolunteers(request):
    volunteers = Volunteer.objects.all()
    print(volunteers)
    return render(request, "volunteers_pg.html", {"volunteers" : volunteers})
