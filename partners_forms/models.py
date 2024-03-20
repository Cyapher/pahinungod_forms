from typing import Any
from django.db import models
from django.core.exceptions import ValidationError
# from django import forms

# Create your models here.
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

    # scope_of_work = models.One(max_length=1, choices=scope_of_work_choices)

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

# FOR PARTNER TYPE
class Type_obj(models.Model):
    type_code = models.CharField(max_length=5)
    type_of_partnership = models.CharField(max_length=64)

    def save(self, *args, **kwargs):
        if self.type_code:
            self.type_code = self.type_code.upper()

        super(Type_obj, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.type_code} : {self.type_of_partnership}"

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

    second_category = [
        ('', 'Select Second Stakeholder Category'),
        ('1', 'NGO',),
        ('1', 'Company'),
        ('1', 'Educational Institution'),
        ('1', 'Others'),
        ('2', 'LGU'),
        ('2', 'National Government Agency'),
        ('2', 'Educational Institution'),
        ('2', 'Others'),
    ]

    # def save(self, *args, **kwargs):
    #     # Populate choices for second_category dynamically based on stakeholder_category
    #     self.second_category = self.get_second_category_choices()
    #     super().save(*args, **kwargs)

    def get_second_category_choices(self):
        print(f'stakeholder_category: {self.stakeholder_category}')

        if self.stakeholder_category == 'Private':
            return [                
                ('NGO', 'NGO'),
                ('Company', 'Company'),
                ('Educational Institution', 'Educational Institution'),
                ('Others', 'Others'),
            ]
            
        elif self.stakeholder_category == 'Government':
            return [
                ('LGU', 'LGU'),
                ('National Government Agency', 'National Government Agency'),
                ('Educational Institution', 'Educational Institution'),
                ('Others', 'Others'),
            ]
        else:
            return []
        
    stakeholder_category = models.CharField(max_length=64, 
                                            choices=stakeholder_category_choices, 
                                            null=True,
                                            blank=False)
    second_category = models.CharField(max_length=64, 
                                       choices=second_category, 
                                       null=True,
                                       blank=False)
    other_choice = models.CharField(max_length=64, 
                                    blank=True,)
    
    # Extra Fields
    type_of_partnership = models.ManyToManyField(Type_obj, blank=True)
    # scope_of_work = models.ManyToManyField(Scope_of_work, blank=True)

    # Date Field
    Agreement_Start_Date = models.DateField()
    Agreement_End_Date = models.DateField()

    # File Field
    files = models.FileField(upload_to='partner_requirements/', blank=False, null=False)
    # files = Multiple_file_field(upload_to='partner_requirements/')


