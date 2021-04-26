from django.urls import path
from . import views
urlpatterns = [
path('viewrec/', views.crimerecord, name = 'crimerecord'),
path('details/<str:crid>/', views.criminaldetails, name = 'CriminalDetails'),
]