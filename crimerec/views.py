from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from crimerec.models import CriminalCase
from crimerec.models import CriminalRecord
from crimerec.filters import CriminalRecordFilter
from addcases.models import Case
from itertools import chain
# from crimerec.filters import CaseFilter

@login_required
def crimerecord(request):
    cr = CriminalRecord.objects.all()
    cc = CriminalCase.objects.all()
    myFilter = CriminalRecordFilter(request.GET, queryset=cr)
    res= []
    
    cr=myFilter.qs
    # [res.append(x) for x in cr if x not in res]

    # cr=mynewFilter.qs
    context = {
            'cr': cr,
            'cc':cc,
            'myFilter':myFilter,
            # 'mynewFilter':mynewFilter
        }
    return render(request, 'crimerec/criminalrec.html',context)

@login_required
def criminaldetails(request,crid):
    
    cr = CriminalRecord.objects.filter(criminal_id = crid).first()
    cc = CriminalCase.objects.filter(criminal_id= crid)
    context = {
            'cr': cr,
            'cc':cc
        }
    return render(request, 'crimerec/criminaldet.html',context)





