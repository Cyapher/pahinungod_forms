from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),

    # PARTNERS
    path('view_partners/', views.view_partners, name='view_partners'),
    path('partner_form/', views.partner_form, name='partner_form'),
    path('add_partner/', views.add_partner, name='add_partner'),
    path('del_partner/<int:partner_id>', views.del_partner, name='del_partner'),
    path('upd_partner/<int:partner_id>', views.upd_partner, name='upd_partner'),
    path('get_second_category_options/', views.get_second_category_options , name='get_second_category_options'),
    
    # TYPE OF PARTNERS
    path('type_form/', views.type_partner_form, name='type_partner_form'),
    path('add_type/', views.add_type, name='add_type'),
    path('del_type/<int:type_id>', views.del_type, name='del_type'),
    path('upd_type/<int:type_id>', views.upd_type, name='upd_type'),
    
    # MISC.
    # path('del_all/', views.del_all, name='del_all'),
    # path('view-pdf/', views.pdf_view, name='pdf_view'),
]

urlpatterns += staticfiles_urlpatterns()