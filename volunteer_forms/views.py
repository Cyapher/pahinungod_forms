import logging
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.db.models import Q

from volunteer_forms.models import Volunteer, Program
from .forms import VolunteerForm, ProgramForm

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
                       'contactNum',
                       'contactEmail']
    
studentFields = ['idNum',
                     'course',
                     'college',
                     'yearLvl']

dateFields = ['startDate',
              'customStartDate']

def homePage(request):

    programs = Program.objects.all()
    return render(request, "volunteerHome.html",
                  {'v_form' : VolunteerForm(),
                   'programs' : programs,
                   'volunteerFields' : volunteerFields,
                   'alumnusFields' : alumnusFields,
                   'pghFields' : pghFields,
                   'workFields' : workFields,
                   'licenseFields' : licenseFields,
                   'insuranceFields' : insuranceFields,
                   'studentFields' : studentFields,
                   'dateFields' : dateFields})

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
        programs = request.POST.getlist('programs')
        if form.is_valid():
            # print("validform")
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
        programs = Program.objects.all()
        return render(request, "volunteerUpdate.html", {"volunteer" : volunteer, 'v_form' : form,
                                                       'programs' : programs,
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

def searchFilter(request):
    query = request.GET.get('q')

    if query:
        volunteers = Volunteer.objects.filter(
            Q(first_name__icontains=query) |
            Q(middle_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(address__icontains=query) |
            Q(age__icontains=query) |
            Q(civilStatus__icontains=query) |
            Q(sex__icontains=query) |
            Q(specification__icontains=query) |
            Q(occupation__icontains=query) |
            Q(otherOccu__icontains=query) |
            Q(programs__name__icontains=query) |
            Q(programs__code__icontains=query) |
            Q(customStartDate__icontains=query)
        ).distinct()
    else:
        volunteers = Volunteer.objects.all()
    
    return render(request, "volunteers_pg.html", {"volunteers" : volunteers})

def printPrograms(request):
    programs = Program.objects.all()
    print(programs)
    return render(request, "programs_pg.html", {"programs" : programs})

def createProgram(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('programs')
    else:
        return render(request, "form_program.html", {"form" : ProgramForm()})

def updateProgram(request, program_id):
    program = Program.objects.get(pk=program_id)

    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)

        if form.is_valid():
            form.save()

            return redirect('programs')
    else:
        form = ProgramForm(instance=program)
        programs = Program.objects.all()
        return render(request, "edit_program.html", {"form" : form, "programs" : programs, "program" : program})
    
def delProgram(request, program_id):
    program = Program.objects.get(pk=program_id)
    program.delete()

    return redirect('programs')

def searchDateRange(request):
    queryStart = request.GET.get('start')
    queryEnd = request.GET.get('end')

    if queryStart and queryEnd:
        volunteers = Volunteer.objects.filter(Q(customStartDate__gte=queryStart) & Q(customStartDate__lte=queryEnd))
    else:
        volunteers = Volunteer.objects.all()
    
    return render(request, "volunteers_pg.html", {"volunteers" : volunteers})

def sort_data(request):
    if request.method == 'GET':
        # Get the values submitted in the form
        column = request.GET.get('column')
        order = request.GET.get('order')

        # Your sorting logic here
        if column == 'first_name':
            sorted_data = Volunteer.objects.all().order_by('first_name' if order == 'asc' else '-first_name')
        elif column == 'customStartDate':
            sorted_data = Volunteer.objects.all().order_by('customStartDate' if order == 'asc' else '-customStartDate')
        elif column == 'occupation':
            sorted_data = Volunteer.objects.all().order_by('occupation' if order == 'asc' else '-occupation')
        else:
            # Handle default case or error
            sorted_data = Volunteer.objects.all()

        return render(request, 'volunteers_pg.html', {'volunteers': sorted_data})


