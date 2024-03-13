from django.db import models

# Create your models here.

class Volunteer(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    mobile = models.CharField(max_length=13)
    telephone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    birthdate = models.DateField(max_length=50)
    # age = models.CharField(max_length=50)

    civilStatusChoices = [
        ('S', 'Single'),
        ('M', 'Married')
    ]

    sexChoices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other/Will not disclose')
    ]

    civilStatus = models.CharField(max_length=1, choices=civilStatusChoices)
    sex = models.CharField(max_length=1, choices=sexChoices)
    bloodType = models.CharField(max_length=3)
    religion = models.CharField(max_length=50)
    healthConditions = models.TextField()
    skillsHobbies = models.TextField()
    foodRestrictions = models.TextField()

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
    contact = models.CharField(max_length=50)

    # license
    prcLicense = models.CharField(max_length=7, blank=True, null=True)
    dept = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    officeAdd = models.CharField(max_length=50, blank=True, null=True)
    license_telephone = models.CharField(max_length=10, blank=True, null=True)
    license_email = models.CharField(max_length=50, blank=True, null=True)
    workSched = models.CharField(max_length=50, blank=True, null=True)

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

    def __str__(self):
        return f"{self.first_name} {self.last_name}"