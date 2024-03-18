from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from volunteer_forms.models import Volunteer
from .forms import VolunteerForm

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

def index(request):
    
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
            return render(request, "form_pg1.html", {"v_form" : form,
                                                    'volunteerFields' : volunteerFields,
                                                    'alumnusFields' : alumnusFields,
                                                    'pghFields' : pghFields,
                                                    'workFields' : workFields,
                                                    'licenseFields' : licenseFields,
                                                    'insuranceFields' : insuranceFields,
                                                    'studentFields' : studentFields})

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
                                                    'studentFields' : studentFields})

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