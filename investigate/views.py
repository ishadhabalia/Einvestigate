import os
# from django.http import FileResponse
from django.conf import settings

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage

from .models import TextEvidence
from .models import FileEvidence
from .models import Suspects
from .models import Leads
from addcases.models import Case
from django.contrib.auth.models import User
from project1.models import CaseStatus 
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

#for download view
from wsgiref.util import FileWrapper
import mimetypes
from django.utils.encoding import force_text, smart_str

timezone.localtime()

def user_passes_investigationedit(view_func):
    def inner(request, case):
        case_obj = Case.objects.filter(case_id = case).first()
        if case_obj.case_io.officer_id == request.user.profile.officer_id:
            context = {
                'case':case,
            }
            return investigationedit(request, case) 
    return inner

def user_passes_investigationdetail(view_func):
    def inner(request, case):
        case_obj = Case.objects.filter(case_id = case).first()
        if case_obj.case_io.officer_id == request.user.profile.officer_id or case_obj.case_dsp_id == request.user.profile.officer_id:
            case_object = Case.objects.filter(case_id = case).first()
            context = {
                'textevidence_edits' : TextEvidence.objects.filter(case_id = case_object),
                'fileevidence_edits' : FileEvidence.objects.filter(case_id = case_object),
                'suspect_edits': Suspects.objects.filter(case_id = case_object),
                'lead_edits': Leads.objects.filter(case_id = case_object),
                'case_statuses' : CaseStatus.objects.filter(case_id = case_object),
                'case':case,   #case id of required case
                'case_object' : Case.objects.filter(case_id = case).first(), #required case instance
            }
            return investigationdetail(request, case)
    return inner
    
# @user_passes_investigationedit
@login_required
def investigationedit(request, case):
    # 'case' variable is case id of required case
    if request.method == 'POST':
        case_object = Case.objects.filter(case_id = case).first() # instance of required case
        if request.POST.get('t_edit_title') and request.POST.get('t_edit_content'):
            post = TextEvidence()
            post.case_id = Case.objects.filter(case_id = case).first() 
            post.edit_id = TextEvidence.objects.filter(case_id = case_object).count() + 1
            post.edit_title = request.POST.get('t_edit_title')
            post.edit_content = request.POST.get('t_edit_content')
            post.save()

        elif request.POST.get('f_edit_title') and request.FILES['f_file_path']:
            post = FileEvidence()
            post.case_id = Case.objects.filter(case_id = case).first() 
            post.edit_id = FileEvidence.objects.filter(case_id = case_object).count() + 1
            post.edit_title = request.POST.get('f_edit_title')
            myfile = request.FILES['f_file_path']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            post.file_name = filename
            post.file_path = fs.url(filename)
            post.save()

        elif request.POST.get('suspect_name') and request.POST.get('suspect_contact') and request.POST.get('suspect_address') and request.POST.get('suspect_reason'):
            post = Suspects()
            post.case_id = Case.objects.filter(case_id = case).first() 
            post.edit_id = Suspects.objects.filter(case_id = case_object).count() + 1
            post.suspect_name = request.POST.get('suspect_name')
            post.suspect_contact = request.POST.get('suspect_contact')
            post.suspect_address = request.POST.get('suspect_address')
            post.suspect_reason = request.POST.get('suspect_reason')
            post.save()

        elif request.POST.get('l_edit_title') and request.POST.get('l_edit_content'):
            post = Leads()
            post.case_id = Case.objects.filter(case_id = case).first() 
            post.edit_id = Leads.objects.filter(case_id = case_object).count() + 1
            post.edit_title = request.POST.get('l_edit_title')
            post.edit_content = request.POST.get('l_edit_content')
            post.save()

        elif request.POST.get('status_title') and request.POST.get('status_content'):
            post = CaseStatus()
            post.case_id = Case.objects.filter(case_id = case).first() 
            post.case_status_no = CaseStatus.objects.filter(case_id = case_object).count() + 1
            post.status_title = request.POST.get('status_title')
            post.status_content = request.POST.get('status_content')
            post.save()
    context = {
        'case':case,
    }
    return render(request, 'investigate/investigationedit.html', context) 


# @user_passes_investigationdetail
@login_required
def investigationdetail(request, case):
    case_object = Case.objects.filter(case_id = case).first()
    context = {
        'textevidence_edits' : TextEvidence.objects.filter(case_id = case_object),
        'fileevidence_edits' : FileEvidence.objects.filter(case_id = case_object),
        'suspect_edits': Suspects.objects.filter(case_id = case_object),
        'lead_edits': Leads.objects.filter(case_id = case_object),
        'case_statuses' : CaseStatus.objects.filter(case_id = case_object),
        'case':case,   #case id of required case
        'case_object' : Case.objects.filter(case_id = case).first(), #required case instance
    }
    return render(request, 'investigate/investigationdetail.html', context)

def download(request, file_name):
    file_path = settings.MEDIA_ROOT +'\\'+ file_name
    file_wrapper = FileWrapper(open(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name) 
    return response

    #fname = os.path.basename(file_path)
    # print(fname)
    # file_path = settings.MEDIA_ROOT + file_name
    # return FileResponse(open(str(file_path), 'rb'))  
  