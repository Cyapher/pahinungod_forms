from django.db import models

# Create your models here.
class Partner(models.Model):
    name = models.CharField(max_length=64)

    partnership_choices = [
        ('HT:BLS', 'Health Training: Basic Life Support'),
        ('HT:BAP', 'Health Training: Breast Advocacy and PFA'),
        ('HT:FAST', 'Health Training: FAST'),
        ('HE:OH', 'Health Education: Oral Health'),
        ('HE:MHPS', 'Health Education: MHPS'),
        ('DPT', 'Disaster Preparedness Training'),
        ('DPL', 'Disaster Preparedness Lecture'),
    ]

    partners = models.CharField(max_length=8, choices=partnership_choices)

    stakeholder_category_choices = [
        ('P', 'Private'),
        ('G', 'Government'),
    ]

    stakeholder_category = models.CharField(max_length=64, choices=stakeholder_category_choices)

    private_category = [
        ('NGO', 'NGO'),
        ('C', 'Company'),
        ('EI', 'Educational Institution'),
    ]

    government_category = [
        ('LGU', 'LGU'),
        ('G', 'National Government Agency'),
        ('E', 'Educational Institution'),
        ('O', 'Others'),
    ]
