from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile
from addcases.models import Case
from project1.models import CaseStatus
from investigate.models import *
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request, 'project1/homepage.html', {'title':'home'})





from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
           
            u_p = user.profile
            form = login(request, user)
            
            if u_p.role==1:
                return HttpResponseRedirect(reverse('admin:index'))
               

            elif u_p.role==2:
                
                # context = {
                #     # 'cases_of_dsp': Case.objects.filter(case_dsp_id = user.profile.officer_id),
                #     'user':user,
                # }
                return redirect('dspprofile')
                # return render(request, 'core/dspprofile.html', context)

            elif u_p.role==3:
                return redirect('ioprofile')
                # # no_of_cases_of_io = Case.objects.filter(case_io = user.profile).count()
                # context = {
                #     # 'number': range(no_of_cases_of_io//3),
                #     # 'three': range(3),
                #     # 'remaining': no_of_cases_of_io%3,
                #     # 'range_rmng': range(no_of_cases_of_io%3),
                #     'cases_of_io' : Case.objects.filter(case_io = user.profile),
                    
                # }
                # return render(request, 'core/ioprofile.html', context)

        else:
            messages.info(request, f'INVALID CREDENTIALS')
    form = AuthenticationForm()
    return render(request, 'core/login.html', {'form':form, 'title':'log in'})

def pagelogout(request):
    logout(request)
    return redirect('home')
    # return render(request, 'project1/homepage.html')

# @login_required
# def dspprofile(request):
#     user=request.user
#     profile = Profile.objects.get(user=request.user)
    
#     context = {
#             'profile': profile,
#             'cases_of_dsp': Case.objects.filter(case_dsp_id = user.profile.officer_id),
#             'title':'dspprofile',
            
#         }
#     return render(request, 'core/dspprofile.html', context)

# @login_required
# def ioprofile(request):
#     user=request.user
#     profile = Profile.objects.get(user=request.user)
    
#     context = {
#             'profile': profile,
#             'cases_of_io' : Case.objects.filter(case_io = user.profile),
#             'title':'ioprofile',
            
#         }
#     return render(request, 'core/ioprofile.html', context)

@login_required

def dspprofile(request):

    user=request.user

    profile = Profile.objects.get(user=request.user)

    

    context = {

            'profile': profile,

            'cases_of_dsp': Case.objects.filter(case_dsp_id = user.profile.officer_id),

            'title':'dspprofile',

            'dspmail': request.user ,

        }

    return render(request, 'core/dspprofile.html', context)



@login_required

def ioprofile(request):

    user=request.user

    # io_email=request.user.email

    profile = Profile.objects.get(user=request.user)

    

    context = {

            'profile': profile,

            'cases_of_io' : Case.objects.filter(case_io = user.profile),

            'title':'dspprofile',

            'iomail': request.user , 

        }

    

    return render(request, 'core/ioprofile.html', context)

@login_required
def profile_view(request):
    u_p = user.profile
    profile = Profile.objects.get(user=request.user)
    context = {
            'profile': profile,
            'cases_of_dsp': Case.objects.filter(case_dsp_id = u_p.officer_id),
            'cases_of_io' : Case.objects.filter(case_io = u_p),
        }
    if u_p.role==2:
        
        template = 'core/dspprofile.html'  
    elif u_p.role==3:
       
        template = 'core/ioprofile.html'
    return render(request, template, context)

@login_required
def profilepage(request):

    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile,
        
    }
    template = 'project1/homepage.html'  
    
    return render(request, template,context)


def password_reset_request(request):

    if request.method == "POST":

        password_reset_form = PasswordResetForm(request.POST)

        if password_reset_form.is_valid():

            data = password_reset_form.cleaned_data['email']

            associated_users = User.objects.filter(Q(email=data))

            if associated_users.exists():

                for user in associated_users:

                    subject = "Password Reset Requested"

                    email_template_name = "registration/password_reset_email.txt"

                    c = {

                    "email":user.email,

                    'domain':'127.0.0.1:8000',

                    'site_name': 'Website',

                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),

                    "user": user,

                    'token': default_token_generator.make_token(user),

                    'protocol': 'http',

                    }

                    email = render_to_string(email_template_name, c)

                    try:

                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)

                    except BadHeaderError:

                        return HttpResponse('Invalid header found.')

                    return redirect ("/password_reset/done/")

    password_reset_form = PasswordResetForm()

    return render(request=request, template_name="registration/password_reset.html", context={"password_reset_form":password_reset_form})