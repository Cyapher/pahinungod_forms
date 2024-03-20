from django import forms
from django.forms import ModelForm, MultipleChoiceField
from volunteer_forms.models import Program, Volunteer

class VolunteerForm(ModelForm):

    class Meta:
        model = Volunteer
        fields = '__all__'


    widgets = {
        'healthConditions' : forms.Textarea(attrs={'rows' : 2}),
        'skillsHobbies' : forms.Textarea(attrs={'rows' : 2}),
        'foodRestrictions' : forms.Textarea(attrs={'rows' : 2})
    }

    placeholders = {
        'first_name' : 'Enter your first name here',
        'middle_name' : 'Enter your middle name here',
        'last_name' : 'Enter your last name here',
        'mobile' : 'Enter your mobile number here',
        'email' : 'Enter your email address here',
        'address' : 'Enter your home address here',
        'telephone' : 'Enter your telephone number here',
        'bloodType' : 'Enter your blood type here',
        'religion' : 'Enter your religion here',
        'constituentUnit' : 'Enter your constituent unit here',
        'specification' : 'Enter your specification here'
    }

    def __init__(self, *args, **kwargs):
        super(VolunteerForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items(): # iterate through all fields on page

            if isinstance(field, forms.CharField):
                field.widget.attrs.update({
                    'class': 'form-control'
                })
            
            if field_name == 'civilStatus':
                field.widget.attrs['class'] = 'form-select'

            if field_name == 'sex':
                field.widget.attrs['class'] = 'form-select'

            if field_name == 'yearLvl':
                field.widget.attrs['class'] = 'form-select'

            if field_name == 'startDate':
                field.widget.attrs['class'] = 'form-select'
                field.widget.attrs['onchange'] = 'dropDate()'

            if field_name == 'constituentUnit':
                field.widget.attrs['id'] = 'multi_col'

            if field_name == 'occupation':
                field.widget.attrs['class'] = 'form-select'
                field.widget.attrs['onchange'] = 'dropWork()'

            if field_name == 'programs':
                field.widget.attrs['size'] = '7'
            
            if field_name in self.placeholders:
                field.widget.attrs['placeholder'] = self.placeholders[field_name]
            
class ProgramForm(ModelForm):

    class Meta:
        model = Program
        fields = '__all__'