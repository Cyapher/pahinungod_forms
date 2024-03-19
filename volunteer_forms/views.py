import logging
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from volunteer_forms.models import Volunteer
from .forms import VolunteerForm

logger = logging.getLogger(__name__)

volunteerFields = ['first_name',
                       'middle_name',
                       'last_name',
                       'mobile',
                       'address',
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
                    'company',
                    'dept', 
                    'officeAdd',
                    'license_telephone',
                    'license_email',
                    'workSched']
    
insuranceFields = ['beneficiaries',
                       'relation',
                       'contact']
    
studentFields = ['idNum',
                     'course',
                     'college',
                     'yearLvl']

dateFields = ['startDate',
              'customStartDate']

def index(request):
    
    return render(request, "form_pg1.html", 
                  {'v_form' : VolunteerForm(),
                   'volunteerFields' : volunteerFields,
                   'alumnusFields' : alumnusFields,
                   'pghFields' : pghFields,
                   'workFields' : workFields,
                   'licenseFields' : licenseFields,
                   'insuranceFields' : insuranceFields,
                   'studentFields' : studentFields,
                   'dateFields' : dateFields})

def createVolunteer(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            print("validform")
            form.save()
            return HttpResponseRedirect(reverse("list"))
        else:
            print("invalidform")
            logger.error("Form submission failed with errors: %s", form.errors)
            return render(request, "form_pg1.html", {"v_form" : form,
                                                    'volunteerFields' : volunteerFields,
                                                    'alumnusFields' : alumnusFields,
                                                    'pghFields' : pghFields,
                                                    'workFields' : workFields,
                                                    'licenseFields' : licenseFields,
                                                    'insuranceFields' : insuranceFields,
                                                    'studentFields' : studentFields,
                                                    'dateFields' : dateFields})

def printVolunteers(request):
    volunteers = Volunteer.objects.all()
    print(volunteers)
    return render(request, "volunteers_pg.html", {"volunteers" : volunteers})

def updateVolunteer(request, volunteer_id):
    volunteer = Volunteer.objects.get(pk=volunteer_id)

    if request.method == 'POST':
        form = VolunteerForm(request.POST, instance=volunteer)

        if form.is_valid():
            form.save()

            return redirect('list')
    else:
        form = VolunteerForm(instance=volunteer)
        return render(request, "edit_volunteer.html", {"volunteer" : volunteer, 'v_form' : form,
                                                   'volunteerFields' : volunteerFields,
                                                    'alumnusFields' : alumnusFields,
                                                    'pghFields' : pghFields,
                                                    'workFields' : workFields,
                                                    'licenseFields' : licenseFields,
                                                    'insuranceFields' : insuranceFields,
                                                    'studentFields' : studentFields,
                                                    'dateFields' : dateFields})

def deleteVolunteer(request, volunteer_id):
    volunteer = Volunteer.objects.get(pk=volunteer_id)
    volunteer.delete()

    return redirect('list')

def view_volunteerInfo(request, volunteer_id):
    volunteer = Volunteer.objects.get(pk=volunteer_id)
    return render(request, "volunteerInfo_card.html", {'volunteer' : volunteer})

def view_volunteerLicense(request, volunteer_id):
    volunteer = Volunteer.objects.get(pk=volunteer_id)
    return render(request, "licenseInfo_card.html", {'volunteer' : volunteer})

def view_volunteerInsurance(request, volunteer_id):
    volunteer = Volunteer.objects.get(pk=volunteer_id)
    return render(request, "insuranceInfo_card.html", {'volunteer' : volunteer})

def view_volunteerStudent(request, volunteer_id):
    volunteer = Volunteer.objects.get(pk=volunteer_id)
    return render(request, "studentInfo_card.html", {'volunteer' : volunteer})