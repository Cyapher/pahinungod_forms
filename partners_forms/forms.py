from django.forms import ModelForm, Select
from .models import Partner, Scope_of_work
from django import forms

class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'

class Scope_of_work(ModelForm):
    class Meta:
        model = Scope_of_work
        fields = '__all__'

def __init__(self, *args, **kwargs):
    super(PartnerForm, self).__init__(*args, **kwargs)

    for field_name, field in self.fields.items():

        if isinstance(field, forms.CharField):
            field.widget.attrs.update({
                'class':'form-control'
            })
        


