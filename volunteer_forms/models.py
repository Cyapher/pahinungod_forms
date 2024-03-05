from django.db import models

# Create your models here.

class License(models.Model):
    prcLicense = models.CharField(max_length=7)
    dept = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    officeAdd = models.CharField(max_length=50)
    telephone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    workSched = models.CharField(max_length=50)

yrChoices = [
    ('1', '1st Year'),
    ('2', '2nd Year'),
    ('3', '3rd Year'),
    ('4', '4th Year'),
    ('5', '5th Year')
]

class Student(models.Model):
    idNum = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
    yearLvl = models.CharField(max_length=1, choices=yrChoices)

class Insurance(models.Model):
    beneficiaries = models.CharField(max_length=50)
    relation = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)

class Volunteer(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    mobile = models.CharField(max_length=13)
    telephone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    birthdate = models.DateField(max_length=50)
    age = models.CharField(max_length=50)

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
    healthConditions = models.CharField(max_length=50)
    skillsHobbies = models.CharField(max_length=50)
    foodRestrictions = models.CharField(max_length=50)

    constituentUnit = models.CharField(max_length=50)
    specification = models.CharField(max_length=50)

    occuChoices = [
        ('PY', 'Physician'),
        ('NR', 'Nurse'),
        ('PH', 'Pharmacist'),
        ('DE', 'Dentist'),
        ('EN', 'ENT'),
        ('TE', 'Teacher'),
        ('OT', 'Other')
    ]

    occupation = models.CharField(max_length=2, choices=occuChoices)
    otherOccu = models.CharField(max_length=50)
    license = models.ForeignKey(License, on_delete=models.CASCADE, related_name="license")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student")
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE, related_name="insurance")