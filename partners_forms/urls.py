from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.partner_form, name='Partner'),
    path('add_partners', views.add_partner, name='add_partner')
]