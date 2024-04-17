from datetime import datetime
from django.shortcuts import render
from volunteer_forms.models import Volunteer
from django.db.models import Q


def dashboard(request):

    volunteers = Volunteer.objects.all()
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_date = datetime.now().date()
    # volunteers = Volunteer.objects.filter(customStartDate__month=current_month, customStartDate__year=current_year)
    volunteers = Volunteer.objects.filter(customStartDate__lt=current_date)

    return render(request, "dashboard.html", {'volunteers' : volunteers})