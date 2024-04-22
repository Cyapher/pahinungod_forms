from django.contrib import admin
from .models import Volunteer, Program
from .models import *
from django.forms import CheckboxSelectMultiple

# Register your models here.

admin.site.register(Program)
admin.site.register(Volunteer)
admin.site.register(AuthUser)