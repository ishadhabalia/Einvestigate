from django.urls import path
from . import views
urlpatterns = [
path('', views.home, name = 'Home'),
path('trackcase/', views.trackcase, name = 'TrackCase'),
path('casestatus/', views.casestatus, name = 'CaseStatus'),
path('casenotfound/', views.casenotfound, name = 'CaseNotFound'),
path('statistics/', views.showstats, name = 'Statistics'),
path('contactus/', views.contactus, name = 'Contact_Us'),
path('aboutus/', views.aboutus, name = 'About_Us'),
path('complaint/', views.onlinecomplaint, name = 'Online_Complaint'),
]