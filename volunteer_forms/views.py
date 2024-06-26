import logging
import os
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator
from faker import Faker

from pahinungod_forms import settings
from volunteer_forms.models import Volunteer, Program
from .forms import VolunteerForm, ProgramForm
from django.contrib.auth.decorators import login_required, user_passes_test


logger = logging.getLogger(__name__)
pagination_count = 5

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

def is_superuser(user):
    
    return user.is_authenticated and (user.is_superuser or user.is_staff)

def homePage(request):
    print(request.META.get('HTTP_USER_AGENT'))
    programs = Program.objects.all()
    return render(request, "volunteerHome.html", {'programs': programs})

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

# def createVolunteer(request):
#     if request.method == "POST":
#         form = VolunteerForm(request.POST)
#         programs = request.POST.getlist('programs')
#         if form.is_valid():
#             # print("validform")
#             form.save()

#             return HttpResponseRedirect(reverse("list"))
#         else:
#             print("invalidform")
#             logger.error("Form submission failed with errors: %s", form.errors)
#             return render(request, "form_pg1.html", {"v_form" : form,
#                                                     'volunteerFields' : volunteerFields,
#                                                     'alumnusFields' : alumnusFields,
#                                                     'pghFields' : pghFields,
#                                                     'workFields' : workFields,
#                                                     'licenseFields' : licenseFields,
#                                                     'insuranceFields' : insuranceFields,
#                                                     'studentFields' : studentFields,
#                                                     'dateFields' : dateFields})

@login_required(login_url='home_vol')
@user_passes_test(is_superuser, login_url='home_vol')
def printVolunteers(request):
    volunteers = Volunteer.objects.all()
    volunteers = volunteers.filter(Q(is_superuser=False) and Q(is_staff=False))

    p = Paginator(volunteers, pagination_count)
    page = request.GET.get("page")
    volunteers = p.get_page(page)

    print(volunteers)
    return render(request, "volunteers_pg.html", {"volunteers" : volunteers})

@login_required(login_url='home_vol')
def updateVolunteer(request, volunteer_id):
    volunteer = Volunteer.objects.get(pk=volunteer_id)

    if request.method == 'POST':
        form = VolunteerForm(request.POST, instance=volunteer)

        if form.is_valid():
            form.save()

            if (is_superuser(request.user)):
                return redirect('list')
            else:
                return redirect('home_vol')

        else:
            logger.error("Form submission failed with errors: %s", form.errors)
    else:
        form = VolunteerForm(instance=volunteer)
        programs = Program.objects.all()
        return render(request, "edit_volunteer.html", {"volunteer" : volunteer, 'v_form' : form,
                                                       'programs' : programs,
                                                   'volunteerFields' : volunteerFields,
                                                    'alumnusFields' : alumnusFields,
                                                    'pghFields' : pghFields,
                                                    'workFields' : workFields,
                                                    'licenseFields' : licenseFields,
                                                    'insuranceFields' : insuranceFields,
                                                    'studentFields' : studentFields,
                                                    'dateFields' : dateFields,
                                                    'pathStart' : "volunteer"})

@login_required(login_url='home_vol')
def updateVolunteerPrograms(request, volunteer_id):
    volunteer = Volunteer.objects.get(pk=volunteer_id)

    if request.method == 'POST':
        form = VolunteerForm(request.POST, instance=volunteer)

        if form.is_valid():
            form.save()

            if (is_superuser(request.user)):
                return redirect('list')
            else:
                return redirect('home_vol')

        else:
            logger.error("Form submission failed with errors: %s", form.errors)
    else:
        form = VolunteerForm(instance=volunteer)
        programs = Program.objects.all()
        return render(request, "edit_vol_program.html", {"volunteer" : volunteer, 'v_form' : form,
                                                       'programs' : programs,
                                                   'volunteerFields' : volunteerFields,
                                                    'alumnusFields' : alumnusFields,
                                                    'pghFields' : pghFields,
                                                    'workFields' : workFields,
                                                    'licenseFields' : licenseFields,
                                                    'insuranceFields' : insuranceFields,
                                                    'studentFields' : studentFields,
                                                    'dateFields' : dateFields,
                                                    'pathStart' : "volunteer"})

@login_required(login_url='home_vol')
@user_passes_test(is_superuser, login_url='home_vol')
def deleteVolunteer(request, volunteer_id):
    volunteer = Volunteer.objects.get(pk=volunteer_id)
    volunteer.delete()

    return redirect('list')

@login_required(login_url='home_vol')
@user_passes_test(is_superuser, login_url='home_vol')
def view_volunteerInfo(request, volunteer_id):
    volunteer = Volunteer.objects.get(pk=volunteer_id)
    return render(request, "volunteerInfo_card.html", {'volunteer' : volunteer})

@login_required(login_url='home_vol')
@user_passes_test(is_superuser, login_url='home_vol')
def view_volunteerLicense(request, volunteer_id):
    volunteer = Volunteer.objects.get(pk=volunteer_id)
    return render(request, "licenseInfo_card.html", {'volunteer' : volunteer})

@login_required(login_url='home_vol')
@user_passes_test(is_superuser, login_url='home_vol')
def view_volunteerInsurance(request, volunteer_id):
    volunteer = Volunteer.objects.get(pk=volunteer_id)
    return render(request, "insuranceInfo_card.html", {'volunteer' : volunteer})

@login_required(login_url='home_vol')
@user_passes_test(is_superuser, login_url='home_vol')
def view_volunteerStudent(request, volunteer_id):
    volunteer = Volunteer.objects.get(pk=volunteer_id)
    return render(request, "studentInfo_card.html", {'volunteer' : volunteer})

@login_required(login_url='home_vol')
@user_passes_test(is_superuser, login_url='home_vol')
def printPrograms(request):
    programs = Program.objects.all()
    print(programs)
    return render(request, "programs_pg.html", {"programs" : programs})

@login_required(login_url='home_vol')
@user_passes_test(is_superuser, login_url='home_vol')
def createProgram(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('programs')
    else:
        return render(request, "form_program.html", {"form" : ProgramForm()})

@login_required(login_url='home_vol')
@user_passes_test(is_superuser, login_url='home_vol')
def updateProgram(request, program_id):
    program = Program.objects.get(pk=program_id)
    prev_path = program.program_img.path if program.program_img else None

    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES, instance=program)
        program_img_input = request.FILES.get("program_img")

        if form.is_valid():
            # If a new image is uploaded, update the program_img field
            if program_img_input:
                previous_image_path = prev_path if program.program_img else None
                print(previous_image_path)

                # Delete the previous image file if it exists
                if previous_image_path:
                    # if os.path.exists(previous_image_path):
                    os.remove(previous_image_path)

                # Save the new image path to the program instance
                form.program_img = program_img_input
                program.delete()
                form.save()

            else:
                form.save()

            return redirect('programs')  # Redirect to the programs list view
    else:
        form = ProgramForm(instance=program)
        return render(request, "edit_program.html", {"form": form, "program": program})

@login_required(login_url='home_vol')
@user_passes_test(is_superuser, login_url='home_vol')
def delProgram(request, program_id):
    program = Program.objects.get(pk=program_id)

    previous_image_path = program.program_img.path.replace(program.program_img.name, "volunteer_forms\\static\\" + program.program_img.name) if program.program_img else None
    
    if previous_image_path:
        os.remove(previous_image_path)
        program.delete()
    
    else:
        program.delete()

    return redirect('programs')

@login_required(login_url='home_vol')
@user_passes_test(is_superuser, login_url='home_vol')
def filterVolunteers(request):
    query = request.GET.get('q')
    queryStart = request.GET.get('start')
    queryEnd = request.GET.get('end')
    column = request.GET.get('column')
    order = request.GET.get('order')

    volunteers = Volunteer.objects.all()
    volunteers = volunteers.filter(Q(is_superuser=False) and Q(is_staff=False))

    if (query):
        print("search = true")
        volunteers = searchFilter(request, volunteers)
    if (column and order):
        print("sort = true")
        volunteers = sort_data(request, volunteers)
    if (queryStart and queryEnd):
        print("date filter = true")
        volunteers = searchDateRange(request, volunteers)

    p = Paginator(volunteers, pagination_count)
    page = request.GET.get("page")
    volunteers = p.get_page(page)

    return render(request, "volunteers_pg.html", {"volunteers" : volunteers})

@login_required(login_url='home_vol')
@user_passes_test(is_superuser, login_url='home_vol')
def searchFilter(request, volunteers):
    query = request.GET.get('q')
    
    if query:
        volunteers = volunteers.filter(
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
        volunteers = volunteers.all()
    
    return volunteers

@login_required(login_url='home_vol')
@user_passes_test(is_superuser, login_url='home_vol')
def searchDateRange(request, volunteers):
    queryStart = request.GET.get('start')
    queryEnd = request.GET.get('end')

    if queryStart and queryEnd:
        volunteers = volunteers.filter(Q(customStartDate__gte=queryStart) & Q(customStartDate__lte=queryEnd))
    else:
        volunteers = volunteers.all()
    
    return volunteers

@login_required(login_url='home_vol')
@user_passes_test(is_superuser, login_url='home_vol')
def sort_data(request, volunteers):
    if request.method == 'GET':
        # Get the values submitted in the form
        column = request.GET.get('column')
        order = request.GET.get('order')

        # Your sorting logic here
        if column == 'first_name':
            sorted_data = volunteers.all().order_by('first_name' if order == 'asc' else '-first_name')
        elif column == 'customStartDate':
            sorted_data = volunteers.all().order_by('customStartDate' if order == 'asc' else '-customStartDate')
        elif column == 'occupation':
            sorted_data = volunteers.all().order_by('occupation' if order == 'asc' else '-occupation')
        else:
            # Handle default case or error
            sorted_data = volunteers.all()

        return sorted_data

def client_view(request, volunteer_id):

    return render(request, "volunteerProfile.html")

def generate_sample_objects(request, num_samples=10):
    # Initialize Faker
    fake = Faker()

    # Generate sample objects and save them to the database
    for _ in range(num_samples):

        # Create and save object to the database
        volunteer = Volunteer.objects.create_user(
                first_name=Faker().first_name(),
                last_name=Faker().first_name(),
                username=Faker().user_name(),           # Random username
                email=Faker().email(),                  # Random email
                password=Faker().password(),            # Random password
                middle_name=Faker().first_name(),       # Random middle name
                address=Faker().address(),              # Random address
                mobile=Faker().phone_number()[:10],          # Random phone number
                telephone=Faker().phone_number()[:10],       # Random phone number
                birthdate=Faker().date_of_birth(),      # Random birthdate
                civilStatus=Faker().random_element(elements=('Single', 'Married')),  # Random civil status
                sex=Faker().random_element(elements=('Male', 'Female', 'Other/Will not disclose')),  # Random sex
                bloodType=Faker().random_element(elements=('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-')),  # Random blood type
                religion=Faker().word(),                # Random religion
                healthConditions=Faker().sentence(),    # Random health conditions
                skillsHobbies=Faker().sentence(),       # Random skills/hobbies
                foodRestrictions=Faker().sentence(),    # Random food restrictions
                constituentUnit=Faker().word(),         # Random constituent unit
                specification=Faker().word(),           # Random specification
                occupation=Faker().random_element(elements=('Physician', 'Nurse', 'Pharmacist', 'Dentist', 'ENT', 'Teacher', 'Other')),  # Random occupation
                otherOccu=Faker().word(),               # Random other occupation
                beneficiaries=Faker().name(),           # Random beneficiaries
                relation=Faker().word(),                # Random relation
                contactNum=Faker().phone_number()[:10],      # Random contact number
                contactEmail=Faker().email(),           # Random contact email
                prcLicense=Faker().random_number(digits=7),  # Random PRC license number
                dept=Faker().word(),                    # Random department
                company=Faker().company(),              # Random company
                officeAdd=Faker().address(),            # Random office address
                license_telephone=Faker().phone_number()[:10],  # Random license telephone
                license_email=Faker().email(),          # Random license email
                workSched=Faker().sentence(),           # Random work schedule
                idNum=Faker().random_number(digits=5),  # Random ID number
                course=Faker().sentence(),              # Random course
                college=Faker().sentence(),             # Random college
                yearLvl=Faker().random_element(elements=('1', '2', '3', '4', '5')),  # Random year level
                startDate=Faker().random_element(elements=('immediately', 'next_week', 'next_month')),  # Random start date
                alumnusCheck=Faker().boolean(),         # Random boolean value
                pghCheck=Faker().boolean(),             # Random boolean value
                workCheck=Faker().boolean(),            # Random boolean value
                licenseCheck=Faker().boolean(),         # Random boolean value
                studentCheck=Faker().boolean()          # Random boolean value
            )
        volunteer.save()
    
    print("Volunteers generated!")