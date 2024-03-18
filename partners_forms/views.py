from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from partners_forms.forms import PartnerForm
from .models import Partner, Scope_of_work

# Create your views here.
def index(request): # Temp landing page
    partners = Partner.objects.all()
    return render(request, "index.html", {'partners' : partners})

def partner_form(request):
    scope_of_work_choices = Scope_of_work.scope_of_work_choices
    # print(f'scope_of_work_choices: {scope_of_work_choices}')
    return render(request, "partners_forms.html", {'form' : PartnerForm(), 'scope_of_work_choices': scope_of_work_choices})

def add_partner(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST, request.FILES)
        uploaded_files = request.FILES.getlist('files')
        if form.is_valid():
            for file in uploaded_files:
                file_instance = Partner(files=file)
                file_instance.save()
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

