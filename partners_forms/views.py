from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from partners_forms.forms import PartnerForm, Type_of_partnerForm
from .models import Partner, Scope_of_work, Type_obj

# Create your views here.
def home_page(request):
    return render(request, "home.html")

def view_partners(request):
    partners = Partner.objects.all()
    return render(request, "view_partners.html", {'partners' : partners})

def partner_form(request):
    scope_of_work_choices = Scope_of_work.scope_of_work_choices
    # print(f'scope_of_work_choices: {scope_of_work_choices}')
    return render(request, "partners_forms.html", {'form' : PartnerForm(), 'scope_of_work_choices': scope_of_work_choices})

def type_partner_form(request):
    types = Type_obj.objects.all()
    return render(request, "type_of_partnership_form.html", {'types': types,'form': Type_of_partnerForm()})

# TYPE OF PARTNERSHIP
def add_type(request):
    form = Type_of_partnerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print('valid')
            form.save()
            return HttpResponseRedirect(reverse('type_partner_form'))
        else:
            return render(request, 'type_of_partnership_form.html', {'form': form})

def del_type(request, type_id):
    if request.method == 'POST':
        to_delete = Type_obj.objects.get(pk=type_id)
        to_delete.delete()
        # return HttpResponseRedirect(reverse('type_partner_form'))
        return redirect('type_partner_form')
    
def upd_type(request, type_id):
    # print(type_id)
    to_update = Type_obj.objects.get(pk=type_id)
    # print(to_update)
    type_form = Type_of_partnerForm(request.POST or None, instance=to_update) # fields
    # print(type_form)
    all_types = Type_obj.objects.all()

    if request.method == 'POST':
        if type_form.is_valid():
            print('type is valid')
            type_form.save()
            return HttpResponseRedirect(reverse('type_partner_form'))
    else:
        return render(request, 'type_of_partnership_form.html', {'type': to_update, 'types': all_types , 'form': type_form})
        # return render(request, 'type_of_partnership_form.html', {'type': to_update, 'form': type_form})
        

# PARTNER
def add_partner(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST, request.FILES)
        # uploaded_files = request.FILES.getlist('files')
        if form.is_valid():
            print('partner valid')
            # FOR MULTIPLE FILES
            # for file in uploaded_files:
            #     file_instance = Partner(files=file)
            #     file_instance.save()

            # FOR ONE FILE
            # file_instance = Partner()

            form.save()
            return HttpResponseRedirect(reverse('view_partners'))
        else:
            print('partner not valid')
            # return render(request, 'partners_forms.html', {'form': form})
            # Form is not valid, print error messages
            for field, errors in form.errors.items():
                # Print error messages for each field
                for error in errors:
                    print(f"Field '{field}': {error}")
            # Render the form again with error messages
            return render(request, 'partners_forms.html', {'form': form})
            
def del_partner(request, partner_id):
    if request.method == 'POST':
        to_delete = Partner.objects.get(pk=partner_id)
        to_delete.delete()
        return HttpResponseRedirect(reverse('partners_form'))

def update_partner(request):
    pass

# def del_all(request):
#     form = Partner.objects.all()
#     form.delete()
#     return render(request, 'index.html')

def get_second_category_options(request):
    print('here in get_secondary')

