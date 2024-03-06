from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from volunteer_forms.models import Volunteer
from .forms import VolunteerForm

def index(request):

    volunteerFields = ['first_name',
                       'middle_name',
                       'last_name',
                       'address',
                       'mobile',
                       'telephone',
                       'email',
                       'birthdate',
                       'age',
                       'civilStatus',
                       'sex',
                       'bloodType',
                       'religion',
                       'healthConditions',
                       'skillsHobbies',
                       'foodRestrictions']
    
    alumnusFields = ['constituentUnit']
    pghFields = ['specification']
    workFields = ['occupation', 'otherOccu']
    
    licenseFields = ['prcLicense',
                    'dept',
                    'company',
                    'officeAdd',
                    'telephone',
                    'email',
                    'workSched']
    
    insuranceFields = ['beneficiaries',
                       'relation',
                       'contact']
    
    studentFields = ['idNum',
                     'course',
                     'college',
                     'yearLvl']
    
    return render(request, "form_pg1.html", 
                  {'v_form' : VolunteerForm(),
                   'volunteerFields' : volunteerFields,
                   'alumnusFields' : alumnusFields,
                   'pghFields' : pghFields,
                   'workFields' : workFields,
                   'licenseFields' : licenseFields,
                   'insuranceFields' : insuranceFields,
                   'studentFields' : studentFields})

def createVolunteer(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("list"))
        else:
            return render(request, "form_pg1.html", {"form" : form})

def printVolunteers(request):
    volunteers = Volunteer.objects.all()
    print(volunteers)
    return render(request, "volunteers_pg.html", {"volunteers" : volunteers})

def clearData(request):
    Volunteer.objects.all().delete()
    
    return HttpResponseRedirect(reverse("list"))
