from django.urls import include, path
from . import views

urlpatterns = [
    path('info', views.dashboard, name="dashboard")
]