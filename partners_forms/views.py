from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from partners_forms.forms import PartnerForm, Type_of_partnerForm, FilesForm
from .models import Partner, Scope_of_work, Type_obj, Files_obj
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

# Create your views here.
# WEB PAGES ================================================================================================================
def home_page(request):
    return render(request, "home.html")

def view_partners(request):
    partners_list = {}
    partners = Partner.objects.all()
    
    for partner in partners:
        files = Files_obj.objects.filter(partner=partner)
        partners_list[partner] = files

    print(f'partners list: {partners_list}')

    # return render(request, "view_partners.html", {'partners' : partners})
    return render(request, "view_partners.html", {'partners' : partners, 'partners_list' : partners_list})

def partner_form(request): # toPartnerForm Questionnairre
    scope_of_work_choices = Scope_of_work.scope_of_work_choices
    # print(f'scope_of_work_choices: {scope_of_work_choices}')
    return render(request, "partners_forms.html", {'form' : PartnerForm(), 'file_form': FilesForm(),'scope_of_work_choices': scope_of_work_choices})

def type_partner_form(request): # toTypePartnerForm Questionnairre
    types = Type_obj.objects.all()
    return render(request, "type_of_partnership_form.html", {'types': types,'form': Type_of_partnerForm()})

# TYPE OF PARTNERSHIP ================================================================================================================
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

# PARTNER ================================================================================================================
def add_partner(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        uploaded_files = request.FILES.getlist('file_field')

        if form.is_valid():
            print('partner valid')
            # print(form.cleaned_data)  # Print cleaned form data
            partner_instance = form.save()
            partner_instance = Partner.objects.get(pk=partner_instance.id)
            print(f'partner instance: {partner_instance}')

            for fi in uploaded_files:
                file_dict = {'file_field': fi}

                files_form = FilesForm(request.POST,file_dict)
                if files_form.is_valid():
                    file_instance = files_form.save()

                form_that_save = Files_obj.objects.get(pk=file_instance.id)
                form_that_save.partner = partner_instance
                form_that_save.save()
            
            # if files_form.is_valid():
            #     print('files valid')
            #     # files_form.partner = partner_instance
            #     # print(f'new partner: {files_form.partner}')
            #     files_form.save()
            # else:
            #     print('files not valid')
            #     print(files_form.cleaned_data)  # Print cleaned form data

            #     for field, errors in files_form.errors.items():
            #         # Print error messages for each field
            #         for error in errors:
            #             print(f"Field '{field}': {error}")

            #     # Form is not valid, render the form again with error messages
            #     return render(request, 'partners_forms.html', {'form': form, 'file_form': files_form})
            
        else:
            print('partner not valid')
            print(form.cleaned_data)  # Print cleaned form data

            for field, errors in form.errors.items():
                # Print error messages for each field
                for error in errors:
                    print(f"Field '{field}': {error}")

            # Form is not valid, render the form again with error messages
            return render(request, 'partners_forms.html', {'form': form, 'file_form': files_form})

        return HttpResponseRedirect(reverse('view_partners'))
        
    else:
        form = PartnerForm()
        files_form = FilesForm()

    return render(request, 'partners_forms.html', {'form': form, 'file_form': files_form})
            
def del_partner(request, partner_id):
    if request.method == 'POST':
        to_delete = Partner.objects.get(pk=partner_id)
        to_delete.delete()
        return redirect('view_partners')

def upd_partner(request, partner_id):
    to_update = Partner.objects.get(pk=partner_id)
    # to_update_files = Files_obj.objects.get(pk=)

    if request.method == 'POST':

        if form.is_valid():
            print('partner is valid')

            storage = FileSystemStorage(location='partner_requirements/')

            form.save()
            return redirect('add_partner')
    else:
        print('partner not valid')
        form = PartnerForm(instance=to_update) # fields
        # files_form = FilesForm(instance=uploaded_files)

        # Form is not valid, print error messages
        for field, errors in form.errors.items():
            # Print error messages for each field
            for error in errors:
                print(f"Field '{field}': {error}")

        # Render the form again with error messages
        return render(request, 'update_partners.html', {'partner': to_update, 'form': form})

# MISC. ================================================================================================================

# def del_all(request):
#     form = Partner.objects.all()
#     form.delete()
#     return render(request, 'index.html')

def get_second_category_options(request):
    print('here in get_secondary')
