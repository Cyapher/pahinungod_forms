import datetime
import os
from typing import Any
from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# from django import forms

# Create your models here.
    
# FOR PARTNER TYPE
class Type(models.Model):
    type_code = models.CharField(max_length=5)
    type_of_partnership = models.CharField(max_length=64)

    def save(self, *args, **kwargs):
        if self.type_code:
            self.type_code = self.type_code.upper()

        super(Type, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.type_code} : {self.type_of_partnership}"
    
# FOR SCOPE OF WORK
class Scope_of_work(models.Model):
    Lecture = 'Lecture'
    Training = 'Training'
    Workshop = 'Workshop'
    Others = 'Others'
    
    scope_of_work_choices = [
        (Lecture, 'Lecture'),
        (Training, 'Training'),
        (Workshop, 'Workshop'),
        (Others, 'Others'),
    ]

# FOR MULTIPLE FILE FIELD
class Multiple_file_field(models.FileField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self, value, instance):
        if value:
            if isinstance(value, (list, tuple)):
                cleaned_files = []
                for file in value:
                    try:
                        self.run_validators(file)
                        cleaned_files.append(file)
                    except ValidationError as e:
                        raise ValidationError({self.name: e})
                return cleaned_files
            else:
                try:
                    self.run_validators(value)
                    return [value]
                except ValidationError as e:
                    raise ValidationError({self.name: e}) 
        else:
            return []

# PARTNER OBJ
class Partner(models.Model):

    # PARTNER NAME
    partner_name = models.CharField(max_length=64)

    # PARTNERSHIP EXTENSION
    partnership_extension_choices = [
        ('', 'Select Partnership Extension'),
        ('Health Training: Basic Life Support', 'Health Training: Basic Life Support'),
        ('Health Training: Breast Advocacy and PFA', 'Health Training: Breast Advocacy and PFA'),
        ('Health Training: FAST', 'Health Training: FAST'),
        ('Health Education: Oral Health', 'Health Education: Oral Health'),
        ('Health Education: MHPS', 'Health Education: MHPS'),
        ('Disaster Preparedness Training', 'Disaster Preparedness Training'),
        ('Disaster Preparedness Lecture', 'Disaster Preparedness Lecture'),
    ]

    partnership_extension = models.CharField(max_length=64, choices=partnership_extension_choices, blank=False)

    # STAKEHOLDER CATEGORY
    stakeholder_category_choices = [
        ('', 'Select Stakeholder Category'),
        ('Private', 'Private'),
        ('Government', 'Government'),
    ]

    second_category_choices = [
        ('', 'Select Second Stakeholder Category'),
        ('NGO', 'NGO',),
        ('Company', 'Company'),
        ('Educational Institution (Private)', 'Educational Institution (Private)'),
        ('LGU', 'LGU'),
        ('National Government Agency', 'National Government Agency'),
        ('Educational Institution (Government)', 'Educational Institution (Government)'),
        ('Others', 'Others'),
    ]
        
    stakeholder_category = models.CharField(max_length=64, 
                                            choices=stakeholder_category_choices, 
                                            null=True,
                                            blank=False)
    second_category = models.CharField(max_length=64, 
                                       choices=second_category_choices, 
                                       null=True,
                                       blank=False)
    other_choice = models.CharField(max_length=64, 
                                    blank=True,)
    
    # Extra Fields
    type_of_partnership = models.ManyToManyField(Type, blank=True)
    # scope_of_work = models.ManyToManyField(Scope_of_work, blank=True)

    # Date Field
    Agreement_Start_Date = models.DateField(default=datetime.date.today, null=False, blank=False)
    Agreement_End_Date = models.DateField(null=False, blank=False)

    # FOREIGN KEY FOR EACH PARTNER
    # Files = models.ForeignKey(Files_obj, on_delete=models.CASCADE, related_name='files') # ano lalagay dito HAHAHA

    def __str__(self):
        return f"{self.partner_name}"

# FOR FILES
class File(models.Model):
    # File Field
    file_field = models.FileField(upload_to="partners_forms/static/partner_requirements") # upload to where?
    file_name = models.CharField(max_length=64,blank=True,null=True)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='partner', blank=True, null=True,)

    def save(self, *args, **kwargs):
        if self.file_field:
            self.file_name = os.path.basename(self.file_field.name)

        super(File, self).save(*args, **kwargs)

    def delete_file(self, *args, **kwargs):
        path = "./partners_forms/static/partner_requirements/" + self.file_name
        print(f'filename: {path}')

        os.remove(path)
        super(File, self).delete(*args, **kwargs)
