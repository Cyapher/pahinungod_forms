from django.forms import ModelForm, Select
from .models import Partner, Scope_of_work

class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'

class Scope_of_work(ModelForm):
    class Meta:
        model = Scope_of_work
        fields = '__all__'
