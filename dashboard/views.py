from django.shortcuts import render
from volunteer_forms.models import Program


def dashboard(request):

    return render(request, "dashboard.html")