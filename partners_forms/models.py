from django.db import models
from django import forms

# Create your models here.
class Partner(models.Model):

    partnership_choices = [
        ('HT:BLS', 'Health Training: Basic Life Support'),
        ('HT:BAP', 'Health Training: Breast Advocacy and PFA'),
        ('HT:FAST', 'Health Training: FAST'),
        ('HE:OH', 'Health Education: Oral Health'),
        ('HE:MHPS', 'Health Education: MHPS'),
        ('DPT', 'Disaster Preparedness Training'),
        ('DPL', 'Disaster Preparedness Lecture'),
    ]

    stakeholder_category_choices = [
        ('P', 'Private'),
        ('G', 'Government'),
    ]

    second_category = [
        ('1', 'NGO',),
        ('1', 'Company'),
        ('1', 'Educational Institution'),
        ('2', 'LGU'),
        ('2', 'National Government Agency'),
        ('2', 'Educational Institution'),
        ('2', 'Others'),
    ]

    def save(self, *args, **kwargs):
        # Populate choices for second_category dynamically based on stakeholder_category
        self.second_category = self.get_second_category_choices()
        super().save(*args, **kwargs)

    def get_second_category_choices(self):
        print(f'stakeholder_category: {self.stakeholder_category}')

        if self.stakeholder_category == 'P':
            return [
                ('NGO', 'NGO'),
                ('C', 'Company'),
                ('EI', 'Educational Institution'),
            ]
        elif self.stakeholder_category == 'G':
            return [
                ('LGU', 'LGU'),
                ('G', 'National Government Agency'),
                ('E', 'Educational Institution'),
                ('O', 'Others'),
            ]
        else:
            return []

        
    # Fields
    name = models.CharField(max_length=64)
    partners = models.CharField(max_length=8, choices=partnership_choices)
    stakeholder_category = models.CharField(max_length=64, 
                                        choices=stakeholder_category_choices, 
                                        null=True)
    second_category = models.CharField(max_length=64, choices=second_category, null=True)
