from django.db import models
# from django import forms

# Create your models here.
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

class type_of_partnership(models.Model):
    type_of_partnership = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.type_of_partnership}"

class Partner(models.Model):

    # PARTNER NAME
    partner_name = models.CharField(max_length=64)

    # PARTNERSHIP EXTENSION
    partnership_extension_choices = [
        ('HT:BLS', 'Health Training: Basic Life Support'),
        ('HT:BAP', 'Health Training: Breast Advocacy and PFA'),
        ('HT:FAST', 'Health Training: FAST'),
        ('HE:OH', 'Health Education: Oral Health'),
        ('HE:MHPS', 'Health Education: MHPS'),
        ('DPT', 'Disaster Preparedness Training'),
        ('DPL', 'Disaster Preparedness Lecture'),
    ]
    partnership_extension = models.CharField(max_length=8, choices=partnership_extension_choices)

    # STAKEHOLDER CATEGORY
    stakeholder_category_choices = [
        ('P', 'Private'),
        ('G', 'Government'),
    ]

    second_category = [
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

        if self.stakeholder_category == 'P':
            return [                
                ('NGO', 'NGO'),
                ('C', 'Company'),
                ('EI', 'Educational Institution'),
                ('O', 'Others'),
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
        
    stakeholder_category = models.CharField(max_length=64, 
                                            choices=stakeholder_category_choices, 
                                            null=True)
    second_category = models.CharField(max_length=64, 
                                       choices=second_category, 
                                       null=True)
    other_choice = models.CharField(max_length=64, 
                                    blank=True)

    type_of_partnership_choices = [
        ('O','Others'),
        ('PT1','Partner Type 1'),
        ('PT2','Partner Type 2'),
    ]

    # type_of_partnership = models.CharField(max_length=4, choices=type_of_partnership_choices, blank=True, null=True)
        
    # Extra Fields

    type_of_partnership = models.ManyToManyField(type_of_partnership, blank=True, null=True)
    # scope_of_work = models.ManyToManyField(Scope_of_work, blank=True)
