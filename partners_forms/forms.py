from django.forms import ModelForm
from .models import *

class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'