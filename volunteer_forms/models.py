from datetime import datetime
from datetime import timedelta
from datetime import date
from django import forms
from django.db import models

# Create your models here.

class Program(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=255)
    program_img = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.code}: {self.name}" 

class Volunteer(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=13)
    telephone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    birthdate = models.DateField(max_length=50)
    age = models.IntegerField(blank=True, null=True)

    civilStatusChoices = [
        ('Single', 'Single'),
        ('Married', 'Married')
    ]

    sexChoices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other/Will not disclose', 'Other/Will not disclose')
    ]

    civilStatus = models.CharField(max_length=50, choices=civilStatusChoices)
    sex = models.CharField(max_length=50, choices=sexChoices)
    bloodType = models.CharField(max_length=3)
    religion = models.CharField(max_length=100)
    healthConditions = models.TextField(blank=True, null=True)
    skillsHobbies = models.TextField(blank=True, null=True)
    foodRestrictions = models.TextField(blank=True, null=True)

    constituentUnit = models.CharField(max_length=50, blank=True, null=True)
    specification = models.CharField(max_length=50, blank=True, null=True)

    occuChoices = [
        ('Physician', 'Physician'),
        ('Nurse', 'Nurse'),
        ('Pharmacist', 'Pharmacist'),
        ('Dentist', 'Dentist'),
        ('ENT', 'ENT'),
        ('Teacher', 'Teacher'),
        ('Other', 'Other')
    ]

    occupation = models.CharField(max_length=50, choices=occuChoices, blank=True, null=True)
    otherOccu = models.CharField(max_length=50, blank=True, null=True)

    beneficiaries = models.CharField(max_length=50)
    relation = models.CharField(max_length=50)
    contactNum = models.CharField(max_length=50)
    contactEmail = models.CharField(max_length=50, blank=True, null=True)

    # license
    prcLicense = models.CharField(max_length=7, blank=True, null=True)
    dept = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    officeAdd = models.CharField(max_length=100, blank=True, null=True)
    license_telephone = models.CharField(max_length=10, blank=True, null=True)
    license_email = models.CharField(max_length=50, blank=True, null=True)
    workSched = models.CharField(max_length=255, blank=True, null=True)

    # student
    yrChoices = [
    ('1', '1st Year'),
    ('2', '2nd Year'),
    ('3', '3rd Year'),
    ('4', '4th Year'),
    ('5', '5th Year')
    ]

    idNum = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=50, blank=True, null=True)
    college = models.CharField(max_length=50, blank=True, null=True)
    yearLvl = models.CharField(max_length=1, choices=yrChoices, blank=True, null=True)

    programs = models.ManyToManyField(Program, blank=True)

    # start date
    startChoices = [
        ('immediately', 'Immediately'),
        ('next_week', 'Next Week'),
        ('next_month', 'Next Month'),
        ('Other', 'Other')
        ]

    startDate = models.CharField(max_length=50, choices=startChoices)
    customStartDate = models.DateField(max_length=50, blank=True, null=True)

    alumnusCheck = models.BooleanField(default=False)
    pghCheck = models.BooleanField(default=False)
    workCheck = models.BooleanField(default=False)
    licenseCheck = models.BooleanField(default=False)
    studentCheck = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        if self.birthdate:
            today = date.today()
            age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
            self.age = age

        if self.startDate == "immediately":

            today = datetime.now().date()

            # Define a list of weekdays (0: Monday, 1: Tuesday, ..., 6: Sunday)
            weekdays = [0, 1, 2, 3, 4]  # Monday to Friday

            # Get the day of the week for the given date (0: Monday, 1: Tuesday, ..., 6: Sunday)
            current_weekday = today.weekday()

            # Calculate the number of days to add to reach the next weekday
            days_to_add = (min((weekday - current_weekday) % 7 for weekday in weekdays) + 1) % 7

            # Add the calculated number of days to the given date
            next_weekday = today + timedelta(days=days_to_add)

            self.customStartDate = next_weekday

        elif self.startDate == "next_week":

            today = datetime.now().date()

            current_weekday = today.weekday()

            # Calculate the number of days to add to reach the next Monday
            days_to_add = (7 - current_weekday) % 7
            
            if current_weekday == 0:
                days_to_add += 7

            # Add the calculated number of days to the given date
            next_monday = today + timedelta(days=days_to_add)

            self.customStartDate = next_monday

        elif self.startDate == "next_month":

            today = datetime.now().date()

            # Get the first day of the next month
            next_month = today.replace(day=1) + timedelta(days=32)
            next_month = next_month.replace(day=1)

            # Find the weekday of the first day of the next month (0: Monday, 1: Tuesday, ..., 6: Sunday)
            first_day_weekday = next_month.weekday()

            # Calculate the number of days to add to reach the next Monday
            days_to_add = (7 - first_day_weekday) % 7

            # Add the calculated number of days to the first day of the next month
            first_monday_next_month = next_month + timedelta(days=days_to_add)

            self.customStartDate = first_monday_next_month

        if self.constituentUnit:
            self.alumnusCheck = True
        else:
            self.alumnusCheck = False

        if self.specification:
            self.pghCheck = True
        else:
            self.pghCheck = False
        
        if self.occupation or self.otherOccu:
            self.workCheck = True
        else:
            self.workCheck = False

        if self.prcLicense or self.company or self.dept or self.officeAdd or self.license_telephone or self.license_email or self.workSched:
            self.licenseCheck = True
        else:
            self.licenseCheck = False
        
        if self.idNum or self.course or self.college or self.yearLvl:
            self.studentCheck = True
        else:
            self.studentCheck = False

        super(Volunteer, self).save(*args, **kwargs)
