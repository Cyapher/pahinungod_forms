from django.urls import include, path
from . import views

urlpatterns = [
    path('pahinungod_home', views.dashboard, name="dashboard")
]