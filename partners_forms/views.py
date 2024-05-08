from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from partners_forms.forms import PartnerForm, Type_of_partnerForm, FilesForm
from .models import Partner, Scope_of_work, Type, File
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout
from django.conf import settings
from django.db.models import Q
from django.core.paginator import Paginator
import os

def is_superuser(user):
    return user.is_authenticated and (user.is_superuser or user.is_staff)

def is_auth(user):
    return not user.is_authenticated

# Create your views here.
# WEB PAGES ================================================================================================================

# PARTNERSHIP EXTENSION
partnership_extension_choices = [
    ('Health Training: Basic Life Support', 'Health Training: Basic Life Support'),
    ('Health Training: Breast Advocacy and PFA', 'Health Training: Breast Advocacy and PFA'),
    ('Health Training: FAST', 'Health Training: FAST'),
    ('Health Education: Oral Health', 'Health Education: Oral Health'),
    ('Health Education: MHPS', 'Health Education: MHPS'),
    ('Disaster Preparedness Training', 'Disaster Preparedness Training'),
    ('Disaster Preparedness Lecture', 'Disaster Preparedness Lecture'),
]

# STAKEHOLDER CATEGORY
stakeholder_category_choices = [
    ('Private', 'Private'),
    ('Government', 'Government'),
]

second_category_choices = [
    ('NGO', 'NGO',),
    ('Company', 'Company'),
    ('Educational Institution (Private)', 'Educational Institution (Private)'),
    ('LGU', 'LGU'),
    ('National Government Agency', 'National Government Agency'),
    ('Educational Institution (Government)', 'Educational Institution (Government)')
]

pagination_count = 2

@user_passes_test(is_superuser, login_url='home_vol')
def home_page(request):
    return render(request, "home.html")

@user_passes_test(is_auth, login_url='dashboard')
def admin_login(request):
    return render(request, "admin_login.html")

def logOutPage(request):
    if request.user.is_superuser or request.user.is_staff:
        logout(request)
        return redirect('admin_login')
    else:
        logout(request)
        return redirect('home_vol')

@user_passes_test(is_superuser, login_url='home_vol')
def view_partners(request):
    partners_list = {}
    partners = Partner.objects.all()

    for partner in partners:
        files = File.objects.filter(partner=partner)
        partners_list[partner] = files

    print(f'partners list: {partners_list}')

    p = Paginator(partners, pagination_count)
    page = request.GET.get("page")
    partners = p.get_page(page)

    types = Type.objects.all()

    # return render(request, "view_partners.html", {'partners' : partners})
    return render(request, "view_partners.html", {'partners' : partners, 
                                                  'types' : types,
                                                  'partners_list' : partners_list, 
                                                  'partnership_extension_choices': partnership_extension_choices,
                                                  'stakeholder_category_choices' : stakeholder_category_choices,
                                                  'second_category_choices' : second_category_choices})

@user_passes_test(is_superuser, login_url='home_vol')
def partner_form(request): # toPartnerForm Questionnairre
    scope_of_work_choices = Scope_of_work.scope_of_work_choices
    # print(f'scope_of_work_choices: {scope_of_work_choices}')
    return render(request, "partners_forms.html", {'form' : PartnerForm()
    , 'file_form': FilesForm(),'scope_of_work_choices': scope_of_work_choices})

@user_passes_test(is_superuser, login_url='home_vol')
def type_partner_form(request): # toTypePartnerForm Questionnairre
    types = Type.objects.all()
    return render(request, "type_of_partnership_form.html", {'types': types,'form': Type_of_partnerForm(), 'action' : "Add"})

# TYPE OF PARTNERSHIP ================================================================================================================
@user_passes_test(is_superuser, login_url='home_vol')
def add_type(request):
    form = Type_of_partnerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print('valid')
            form.save()
            return HttpResponseRedirect(reverse('type_partner_form'))
        else:
            return render(request, 'type_of_partnership_form.html', {'form': form, 'action' : "Add"})

@user_passes_test(is_superuser, login_url='home_vol')
def del_type(request, type_id):
    if request.method == 'POST':
        to_delete = Type.objects.get(pk=type_id)
        to_delete.delete()
        # return HttpResponseRedirect(reverse('type_partner_form'))
        return redirect('type_partner_form')

@user_passes_test(is_superuser, login_url='home_vol')   
def upd_type(request, type_id):
    # print(type_id)
    to_update = Type.objects.get(pk=type_id)
    # print(to_update)
    type_form = Type_of_partnerForm(request.POST or None, instance=to_update) # fields
    # print(type_form)
    all_types = Type.objects.all()

    if request.method == 'POST':
        if type_form.is_valid():
            print('type is valid')
            type_form.save()
            return HttpResponseRedirect(reverse('type_partner_form'))
    else:
        return render(request, 'type_of_partnership_form.html', {'type': to_update, 'types': all_types , 'form': type_form, 'action' : "Edit"})
        # return render(request, 'type_of_partnership_form.html', {'type': to_update, 'form': type_form})  

# PARTNER ================================================================================================================
@user_passes_test(is_superuser, login_url='home_vol')
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

                files_form = FilesForm(request.POST, file_dict)
                if files_form.is_valid():
                    file_instance = files_form.save()

                form_that_save = File.objects.get(pk=file_instance.id)
                form_that_save.partner = partner_instance
                form_that_save.save()
        
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

@user_passes_test(is_superuser, login_url='home_vol')
def upd_partner(request, partner_id):
    # Instances
    to_update = Partner.objects.get(pk=partner_id) # Partner Instance
    # print(f'to update: {partner_id}')
    uploaded_files = File.objects.filter(partner=to_update) # Files Instance
    # print(f'to update: {uploaded_files}')
    updated_files = request.FILES.getlist('file_field')
    print(f'updated files: {updated_files}')

    # If ok ung mga fields
    if request.method == 'POST':
        # Forms
        form = PartnerForm(request.POST or None, instance=to_update) # Partner Form
        # files_form = FilesForm(request.POST or None, instance=uploaded_files)

        if form.is_valid():
            print('partner valid')
            partner_instance = form.save()
            partner_instance = Partner.objects.get(pk=partner_instance.id)
            # print(f'partner instance: {partner_instance.id}')

            # Delete Document
            for file in uploaded_files:
                # file.delete()
                file.delete_file()

            # Update
            for fi in updated_files:
                # Dictionary of files
                file_dict = {'file_field': fi}

                files_form = FilesForm(request.POST or None, file_dict)
                if files_form.is_valid():
                    print('files is valid')
                    file_instance = files_form.save()
                    print(f'file instance: {file_instance}')
                else:
                    print(f'File form errors: {files_form.errors}')
                
                form_that_save = File.objects.get(pk=file_instance.id)
                form_that_save.partner = to_update
                form_that_save.save()

            return HttpResponseRedirect(reverse('view_partners'))
    
    # If papunta sa form
    else:
        form = PartnerForm(instance=to_update) # fields
        files_form = FilesForm(request.POST or None, request.FILES)

        # Render the form again with error messages
        return render(request, 'update_partners.html', {'partner': to_update, 'form': form, 'file_form': files_form})

@user_passes_test(is_superuser, login_url='home_vol')
def del_partner(request, partner_id):
    if request.method == 'POST':
        to_delete = Partner.objects.get(pk=partner_id)
        files = File.objects.filter(partner=to_delete)
        print(f'Files List: {files}')

        # Delete Document
        for file in files:
            # file.delete()
            file.delete_file()

        # Delete Partner
        to_delete.delete()

        return redirect('view_partners')

@user_passes_test(is_superuser, login_url='home_vol')
def filterPartners(request):
    # get all partners
    partners = Partner.objects.all()
    partners_list = {}

    # Get all files of specified partners
    for partner in partners:
        files = File.objects.filter(partner=partner)
        partners_list[partner] = files

    # Check Action (Search, Filter, Sort)
    if(query):
        partners = partners.filter(partner_name__contains=query)
        pass

    # Search Partners
    # partners = partners.filter(partner_name__contains=query)
    
    return render(request, "view_partners.html", {'partners': partners, 'partners_list' : partners_list})

@user_passes_test(is_superuser, login_url='home_vol')
def searchFilter(request, partners):
    query = request.GET.get('q')
    print(f'query: {query}')

    # Filter Partner
    # +++++ Partnership Extension +++++
    partner_extensions = request.GET.getlist('partnership_extensions')
    for extension in partner_extensions:
        print(f'partnership extensions: {extension}')
        # print(partner_extensions)

    # +++++ Date (Start & End) +++++
    start = request.GET.get('start')
    end = request.GET.get('end')

    # +++++ Category (Primary & Secondary) +++++
    category_radio = request.GET.get('category_radio')
    primary_list = request.GET.getlist('primary_categories')
    secondary_list = request.GET.getlist('secondary_categories')

    # +++++ Partnership Type +++++
    type_list = request.GET.getlist('type_filters')

    # +++++ Partnership Type +++++
    column = request.GET.get('column')
    order = request.GET.get('order')

    # Check Action (Search, Filter, Sort)
    if(query): # Search Partners
        # partners = partners.filter(partner_name__contains=query)
        partners = searchFilter(request, partners, query)
    if(partner_extensions):
        partners = partner_extensions_query(request, partners, partner_extensions)
    if(start or end):
        partners = dateFilter(request, partners, start, end)
    if(category_radio):
        partners = categoryFilter(request, category_radio, primary_list, secondary_list, partners)
    if(type_list):
        partners = typeFilter(request, partners, type_list)
    if(column and order):
        partners = sortPartners(request, partners, column, order)

    p = Paginator(partners, pagination_count)
    page = request.GET.get("page")
    partners = p.get_page(page)

    types = Type.objects.all()
    return render(request, "view_partners.html", {'partners': partners, 
                                                  'types' : types,
                                                  'category_radio' : category_radio,
                                                  'partnership_filters' : partner_extensions,
                                                  'primary_filters' : primary_list,
                                                  'secondary_filters' : secondary_list,
                                                  'type_filters' : type_list,
                                                  'partners_list' : partners_list, 
                                                  'partnership_extension_choices': partnership_extension_choices,
                                                  'stakeholder_category_choices' : stakeholder_category_choices,
                                                  'second_category_choices' : second_category_choices})
    # return HttpResponseRedirect(reverse('view_partners'))

def searchFilter(request, partners, query):

    partners = partners.filter(
        Q(partner_name__icontains=query) |
        Q(partnership_extension__icontains=query) | 
        Q(stakeholder_category__icontains=query) | 
        Q(second_category__icontains=query) | 
        Q(other_choice__icontains=query) | 
        Q(type_of_partnership__type_code__icontains=query) | 
        Q(type_of_partnership__type_of_partnership__icontains=query)
        ).distinct()

    if partners:
        print('partner exists')
        print(f'partners: {partners}')
        return partners
    elif query == '':
        partners = partners.all()
    else:
        print('no partner with this query')
        return None
    
    return partners

def partner_extensions_query(request, partners, query):

    q_objects = Q()

    for value in query:
        q_objects |= Q(partnership_extension=value)

    partners = partners.filter(q_objects)
    
    if partners:
        return partners
    else:
        return None

def typeFilter(request, partners, query):

    q_objects = Q()

    for value in query:
        q_objects |= Q(type_of_partnership__type_code=value)

    partners = partners.filter(q_objects)

    print("===========")
    print(q_objects)

    if partners:
        return partners
    else:
        return None

def dateFilter(request, partners, start, end):
    if start and end:
        partners = partners.filter(Q(Agreement_Start_Date__gte=start) & Q(Agreement_End_Date__lte=end))
    elif start:
        partners = partners.filter(Q(Agreement_Start_Date__gte=start))
    elif end:
        partners = partners.filter(Q(Agreement_End_Date__lte=end))

    if partners:
        return partners
    else:
        return None
    
def categoryFilter(request, category_radio, primary_list, secondary_list, partners):

    q_objects = Q()

    if(category_radio=='1'):
        for value in primary_list:
            q_objects |= Q(stakeholder_category=value)
    elif(category_radio=='2'):
        for value in secondary_list:
            q_objects |= Q(second_category=value)

    partners = partners.filter(q_objects)

    if partners:
        return partners
    else:
        return None

def sortPartners(request, partners, column, order):

    if partners:

        partners = partners.order_by(column if order == 'asc' else ('-' + column))
        return partners

    else:
        return None

# MISC. ================================================================================================================

# def del_all(request):
#     form = Partner.objects.all()
#     form.delete()
#     return render(request, 'index.html')

def get_second_category_options(request):
    print('here in get_secondary')
