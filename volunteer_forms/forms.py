from django import forms
from django.forms import ModelForm
from volunteer_forms.models import Volunteer, License, Student, Insurance


class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        # fields = '__all__'
        exclude = ['license', 'student', 'insurance']

class LicenseForm(ModelForm):
    class Meta:
        model = License
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class InsuranceForm(ModelForm):
    class Meta:
        model = Insurance
        fields = '__all__'