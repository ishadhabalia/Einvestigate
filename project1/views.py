from django.shortcuts import render,redirect
from django.http import HttpResponse
from addcases.models import Case
from .models import CaseStatus
from django.contrib.auth.models import User

def home(request):
     return render(request,'project1/homepage.html')
def login(request):
     return render(request,'project1/login.html')
def trackcase(request):
     if request.method == 'POST':
          flag=0
          if request.POST.get('tracking_id') and request.POST.get('passcode'):
               tracking_id_input = request.POST.get('tracking_id')
               passcode_input = request.POST.get('passcode')

               case_match = Case.objects.filter(tracking_id=tracking_id_input)
               case_match = case_match.filter(passcode=passcode_input).first()
               if not case_match:
                    flag=1
                    return render(request, 'project1/casenotfound.html') 
               else:
                    casedetails = {
                         'case' : case_match,
                         'statuses' : CaseStatus.objects.filter(case_id = case_match),
                    }
                    return render(request, 'project1/casestatus.html', casedetails)  
     else:
          return render(request,'project1/trackcase.html')


def casestatus(request, casedetails):
     casedetails = {
          'case' : case_match,
          'statuses' : CaseStatus.objects.filter(case_id = case_match),
     }
     return render(request, 'project1/casestatus.html', casedetails)  

def casenotfound(request):
    return redirect('trackcase')

def showstats(request):
     case_obj = Case.objects.all()
     rob=0
     dom_vio=0
     corruption=0
     poaching=0
     child_abuse=0
     cyber_crime=0
     sex_asst=0
     terrorism=0
     violent_crime=0

     for stats in case_obj:
          if stats.case_category == 'Robbery':
               rob+=1
          elif stats.case_category == 'Domestic violence':
               dom_vio+=1
          elif stats.case_category == 'Corruption':
               corruption+=1
          elif stats.case_category == 'Poaching':
               poaching+=1
          elif stats.case_category == 'Child Abuse':
               child_abuse+=1
          elif stats.case_category == 'Sexual Assault':
               sex_asst+=1
          elif stats.case_category == 'Terrorism':
               terrorism+=1
          elif stats.case_category == 'Cyber-crime':
               cyber_crime+=1
          else :
               violent_crime+=1


     context = {
          'rob':rob,
          'dom_vio':dom_vio,
          'corruption':corruption,
          'poaching':poaching,
          'child_abuse':child_abuse,
          'sex_asst':sex_asst,
          'terrorism':terrorism,
          'cyber_crime':cyber_crime,
          'violent_crime':violent_crime,
     }
     # context={'case':case}
    
     # obj = Case.objects.get(case_id=case).first()
     #  case_object = Case.objects.filter(case_id = case).first()
     # category = obj.case_category
     template = 'project1/statistics.html'
#      casedetails = {
#         'case':case,
#         'obj' : Case.objects.filter(case_id = case).first(),
#     }
     return render(request, template,context)               
    
def contactus(request):
     return render(request,'project1/contactus.html')
     
def aboutus(request):
     return render(request,'project1/aboutus.html')
