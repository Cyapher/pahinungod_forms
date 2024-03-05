from django.forms import ModelForm
from volunteer_forms.models import Volunteer


class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        # fields = '__all__'
        exclude = ['license', 'student', 'insurance']