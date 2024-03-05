from django.shortcuts import render
from .forms import VolunteerForm

def index(request):
    return render(request, "form_pg1.html", {'form' : VolunteerForm()})
    
