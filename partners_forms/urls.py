from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),

    # PARTNERS
    path('view_partners/', views.view_partners, name='view_partners'),
    path('partner_form/', views.partner_form, name='partner_form'),
    path('add_partners/', views.add_partner, name='add_partner'),
    path('get_second_category_options/', views.get_second_category_options , name='get_second_category_options'),
    
    # TYPE OF PARTNERS
    path('type_form/', views.type_partner_form, name='type_partner_form'),
    path('add_type/', views.add_type_of_partner, name='add_type_of_partner'),
    
    # MISC.
    path('del_all/', views.del_all, name='del_all'),
]

urlpatterns += staticfiles_urlpatterns()