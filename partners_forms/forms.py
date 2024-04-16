from django.forms import ModelForm, Select, ClearableFileInput
from .models import Partner, Scope_of_work, Type, File
from django import forms

class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'

    placeholders = {
        'partner_name' : 'Enter Partner Name', 
        'partnership_extension' : 'Enter Partnership Extension Here',
        'other_choice' : 'Enter Second Category Choice Here',
        'type_of_partnership' : 'Enter Type of Partnership Here',
        'Agreement_Start_Date' : 'Start',
        'Agreement_End_Date' : 'End',
    }

    def __init__(self, *args, **kwargs):
        super(PartnerForm, self).__init__(*args, **kwargs)

        # For all field and field_name
        for field_name, field in self.fields.items():
            if isinstance(field, forms.CharField):
                field.widget.attrs.update({
                    'class':'form-control'
                })

            if isinstance(field, forms.ChoiceField):
                field.widget.attrs.update({
                    'class':'form-control'
                })

            if field_name in self.placeholders:
                field.widget.attrs['placeholder'] = self.placeholders[field_name]
        
            self.fields['partnership_extension'].widget.attrs['initial'] = {'default'}
            self.fields['partnership_extension'].empty_label = 'Select Partnership Extension'

            # self.fields['files'].widget.attrs['multiple'] = True

            # For File Upload
            # self.fields['files'] = ClearableFileInput(attrs={'multiple': True})

class Type_of_partnerForm(ModelForm):
    class Meta:
        model = Type
        fields = '__all__'

    placeholders = {
        'type_code' : 'Enter Partner Type Code', 
        'type_of_partnership' : 'Enter Partnership Type',
    }    
    
    def __init__(self, *args, **kwargs):
        super(Type_of_partnerForm, self).__init__(*args, **kwargs)

        # For all field and field_name
        for field_name, field in self.fields.items():
            if isinstance(field, forms.CharField):
                field.widget.attrs.update({
                    'class':'form-control'
                })

            if field_name in self.placeholders:
                field.widget.attrs['placeholder'] = self.placeholders[field_name]

class FilesForm(ModelForm):
    class Meta:
        model = File
        fields = ['file_field']


    def __init__(self, *args, **kwargs):
        super(FilesForm, self).__init__(*args, **kwargs)

        # For File Upload
        # self.fields['files'] = ClearableFileInput(attrs={'multiple': True})
        self.fields['file_field'].widget.attrs['multiple'] = True
   

class Scope_of_work(ModelForm):
    class Meta:
        model = Scope_of_work
        fields = '__all__'

    



