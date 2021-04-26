from django.urls import path
from . import views
urlpatterns = [
path('addcase/', views.addcase, name = 'Addcase'),
path('caseadded/', views.caseadded, name = 'CaseAdded'),
path('casenotadded/', views.casenotadded, name = 'caseNotAdded'),
]