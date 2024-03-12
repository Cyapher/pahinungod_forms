from django.forms import ModelForm, Select
from .models import Partner

class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'
        # widgets = {
        #     # 'stakeholder_category' : Select(attrs={'onchange' : 'stakeholder_category_options(this);'}),
        #     # 'second_category' : Select(attrs={'onchange' : 'second_category_options();'}),
        # }

