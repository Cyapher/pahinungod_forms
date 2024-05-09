from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from volunteer_forms.models import Program, Volunteer

class VolunteerForm(ModelForm):

    class Meta:

        programs = forms.ModelMultipleChoiceField(
            widget = forms.CheckboxSelectMultiple,
            queryset = Program.objects.all()
        )

        model = Volunteer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['required'] = False
        self.fields['password'].widget.attrs['required'] = False
        self.fields['date_joined'].widget.attrs['required'] = False


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
        'specification' : 'Enter your specification here',
        'prcLicense' : 'Enter your PRC License # here',
        'dept' : 'Enter your department here',
        'company' : 'Enter your company name here',
        'officeAdd' : 'Enter your office address here',
        'license_telephone' : 'Enter your company phone # here',
        'license_email' : 'Enter your company email address here',
        'workSched' : 'Enter your work schedule here',
        'idNum' : 'Enter your ID # here',
        'course' : 'Enter your course/program here',
        'college' : 'Enter your college here',
        'yearLvl' : 'Enter your year level here'
    }

    licenseStudentFields = ['prcLicense',
                    'company',
                    'dept', 
                    'officeAdd',
                    'license_telephone',
                    'license_email',
                    'workSched',
                    'beneficiaries',
                    'relation',
                    'contactNum',
                    'contactEmail',
                    'idNum',
                    'course',
                    'college',
                    'yearLvl']

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

            if field_name == 'occupation':
                field.widget.attrs['class'] = 'form-select'
                field.widget.attrs['onchange'] = 'dropWork()'

            if field_name == 'programs':
                field.widget.attrs['size'] = '7'

            if field_name == 'address':
                field.widget.attrs['style'] = 'width: 100%'

            if field_name == 'telephone':
                field.widget.attrs['style'] = 'width: 100%'

            if field_name == 'bloodType':
                field.widget.attrs['style'] = 'width: 100%'

            if field_name == 'constituentUnit':
                field.widget.attrs['style'] = 'width: 100%'

            if field_name == 'otherOccu':
                field.widget.attrs['style'] = 'width: 100%'

            if field_name == 'specification':
                field.widget.attrs['style'] = 'width: 100%'
            
            if field_name in self.placeholders:
                field.widget.attrs['placeholder'] = self.placeholders[field_name]
            
            if field_name in self.licenseStudentFields:
                field.widget.attrs['style'] = 'width: 100%'

class ProgramForm(ModelForm):

    class Meta:
        model = Program
        fields = '__all__'

    program_placeholders = {
        'code' : 'Enter the program code here',
        'name' : 'Enter the program name here',
        'description' : 'Enter the description here'
    }

    def __init__(self, *args, **kwargs):
        super(ProgramForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items(): # iterate through all fields on page

            if isinstance(field, forms.CharField):
                field.widget.attrs.update({
                    'class': 'form-control',
                })

            if field_name in self.program_placeholders:
                field.widget.attrs['placeholder'] = self.program_placeholders[field_name]