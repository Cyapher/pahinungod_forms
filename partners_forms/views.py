from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from partners_forms.forms import PartnerForm
from .models import Partner

# Create your views here.
def index(request): # Temp landing page
    partners = Partner.objects.all()
    display = partners
    return render(request, "index.html", {'partners' : partners})

def partner_form(request):
    return render(request, "partners_forms.html", {'form' : PartnerForm()})

def add_partner(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'partners_forms.html', {'form': form})
        
def del_all(request):
    form = Partner.objects.all()
    form.delete()
    return render(request, 'index.html')

def get_second_category_options(request):
    print('here in get_secondary')
