from django.contrib import admin
from .models import Partner, Scope_of_work, Type, File

# Register your models here.
admin.site.register(Partner)
admin.site.register(Scope_of_work)
admin.site.register(Type)
admin.site.register(File)
