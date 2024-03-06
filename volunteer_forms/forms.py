from django import forms
from django.forms import ModelForm
from volunteer_forms.models import Volunteer


class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = '__all__'

    placeholders = {
        'first_name' : 'Enter your first name here'
    }

    def __init__(self, *args, **kwargs):
        super(VolunteerForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.CharField):
                field.widget.attrs.update({
                    'class': 'form-control'
                })
            if field_name in self.placeholders:
                field.widget.attrs['placeholder'] = self.placeholders[field_name]