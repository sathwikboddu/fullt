from django.urls import path
from . import views

app_name = 'sathwik'

urlpatterns = [
    path('retrieve', views.retrieve, name='retrieve')
]