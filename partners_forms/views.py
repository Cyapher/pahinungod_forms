from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from partners_forms.forms import PartnerForm, Type_of_partnerForm
from .models import Partner, Scope_of_work, Type_obj
from django.core.files.storage import FileSystemStorage

# Create your views here.
# WEB PAGES ================================================================================================================
def home_page(request):
    return render(request, "home.html")

def view_partners(request):
    partners = Partner.objects.all()
    for partner in partners:
        partner.files_list = [url.strip() for url in partner.files_list.split('\n')]
        print(f'IN VIEW: {partner.files_list}')

    return render(request, "view_partners.html", {'partners' : partners})

def partner_form(request):
    scope_of_work_choices = Scope_of_work.scope_of_work_choices
    # print(f'scope_of_work_choices: {scope_of_work_choices}')
    return render(request, "partners_forms.html", {'form' : PartnerForm(), 'scope_of_work_choices': scope_of_work_choices})

def type_partner_form(request):
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
        form = PartnerForm(request.POST, request.FILES)
        uploaded_files = request.FILES.getlist('files')
        updated_files_list = ''

        if form.is_valid():
            print('partner valid')

            storage = FileSystemStorage(location='partner_requirements/')

            # FOR MULTIPLE FILES
            for file in uploaded_files:
                filename = storage.save(file.name, file)
                new_file_url = storage.url(filename)

                print(f' In Loop: \n {new_file_url}')

                # Append list (text field)
                updated_files_list += new_file_url + '\n'
                
            updated_files_list = updated_files_list[:-1]
            print(f'\n Files List: \n {updated_files_list}')
            
            # Update files_list
            form.instance.files_list = updated_files_list

            form.save()
            return HttpResponseRedirect(reverse('view_partners'))
            # return HttpResponseRedirect(reverse('view_partners', {'file_arr': file_list}))
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
        return redirect('view_partners')

def upd_partner(request, partner_id):
    to_update = Partner.objects.get(pk=partner_id)
    form = PartnerForm(request.POST or None, request.FILES or None, instance=to_update) # fields
    uploaded_files = request.FILES.getlist('files')
    updated_files_list = ''
    
    if request.method == 'POST':

        if form.is_valid():
            print('partner is valid')

            storage = FileSystemStorage(location='partner_requirements/')

            # FOR MULTIPLE FILES
            for file in uploaded_files:
                filename = storage.save(file.name, file)
                new_file_url = storage.url(filename)

                print(f' In Loop: \n {new_file_url}')

                # Append list (text field)
                updated_files_list += new_file_url + '\n'
                
            updated_files_list = updated_files_list[:-1]
            print(f'\n Files List: \n {updated_files_list}')
            
            # Update files_list
            form.instance.files_list = updated_files_list

            form.save()
            return redirect('view_partners')
    else:
        print('partner not valid')
        # return render(request, 'partners_forms.html', {'form': form})

        # Form is not valid, print error messages
        # for field, errors in form.errors.items():
        #     # Print error messages for each field
        #     for error in errors:
        #         print(f"Field '{field}': {error}")

        # Render the form again with error messages
        return render(request, 'update_partners.html', {'partner': to_update, 'form': partner_form})

# MISC. ================================================================================================================

# def del_all(request):
#     form = Partner.objects.all()
#     form.delete()
#     return render(request, 'index.html')

def get_second_category_options(request):
    print('here in get_secondary')

# def pdf_view(request):
#     with open("C:\Users\LENOVO\Documents\GitHub\pahinungod_forms\partner_requirements\WPR5(03_18 - 03_22)_Diaz.docx (1).pdf", ):
#         response = HttpResponse(pdf.read(), content_type='application/pdf')
#         response['Content-Disposition'] = 'inline;filename=WPR5(03_18 - 03_22)_Diaz.docx (1).pdf'
#         return response