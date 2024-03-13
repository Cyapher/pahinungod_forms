from django.contrib import admin
from .models import Partner, Scope_of_work, type_of_partnership

# Register your models here.
admin.site.register(Partner)
admin.site.register(Scope_of_work)
admin.site.register(type_of_partnership)
