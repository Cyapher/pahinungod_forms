from django.contrib import admin
from .models import Volunteer, Insurance, Student, License

# Register your models here.

admin.site.register(Volunteer)
admin.site.register(Insurance)
admin.site.register(Student)
admin.site.register(License)