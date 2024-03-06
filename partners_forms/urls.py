from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.partner_form, name='Partner'),
    path('add_partners/', views.add_partner, name='add_partner'),
    path('del_all/', views.del_all, name='del_all'),
    path('get_second_category_options/', views.get_second_category_options , name='get_second_category_options'),
]