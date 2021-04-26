from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Case
from django.contrib.auth.decorators import user_passes_test
from django.utils.crypto import get_random_string
import uuid
from core.models import Profile
from django.contrib.auth.decorators import login_required
from MP_new.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from django.utils import timezone
timezone.localtime()

def user_role_check(user):
    return user.profile.role==2

# Create your views here.
@login_required
@user_passes_test(user_role_check)
def addcase(request):
    if request.method == 'POST':
        flag=0
        if request.POST.get('case_category') and request.POST.get('case_description') and request.POST.get('crime_location') and request.POST.get('crime_district') and request.POST.get('crime_date') and request.POST.get('complainant_name') and request.POST.get('complainant_contact') and request.POST.get('complainant_email') and request.POST.get('case_io_id') and request.POST.get('case_io_username'):
            post=Case()
            
            prefix = 'C{}'.format(timezone.now().strftime('%d%m%y'))
            count = Case.objects.all().count() + 1
            post.case_id = prefix + '{0:06d}'.format(count)
            post.case_dsp_id=request.user.profile.officer_id
            post.case_category=request.POST.get('case_category')
            post.case_description=request.POST.get('case_description')
            post.crime_location = request.POST.get('crime_location')
            post.crime_district=request.POST.get('crime_district')
            post.crime_date = request.POST.get('crime_date')
            post.complainant_name = request.POST.get('complainant_name')
            post.complainant_contact = request.POST.get('complainant_contact')
            post.complainant_email = request.POST.get('complainant_email')
            post.accused_name = request.POST.get('accused_name')
            post.accused_contact = request.POST.get('accused_contact')
            post.accused_email = request.POST.get('accused_email')


            temp_io_username = request.POST.get('case_io_username')
            temp_io_id = request.POST.get('case_io_id')
            iodetails = Profile.objects.filter(officer_id=temp_io_id).first()
            if not iodetails:
                flag=1
            elif iodetails.user.username!=temp_io_username:
                flag=1
            else:
                post.case_io=iodetails

            post.tracking_id = uuid.uuid4()
            post.passcode = get_random_string(length=8)
     
            if flag==0:
                post.save()

                subject = 'Case Filed Digitally'
                message = f'Hello {post.complainant_name} \n\nYour case has been opened for investigation! \n\nYou can track the case status with this link: \nhttp://127.0.0.1:8000/trackcase/  \n\nYou need to add following credentials: \nTracking ID: {post.tracking_id} \nCode: {post.passcode}'
                recepient = post.complainant_email
                send_mail(subject, 
                message, EMAIL_HOST_USER, [recepient], fail_silently = False)

                if post.accused_email!="":
                    subject = 'Case filed against you'
                    message = f'Hello {post.accused_name} \n\nA case has been registered against you and is being investigated! \n\nYou can track the case status with this link: \nhttp://127.0.0.1:8000/trackcase/  \n\nYou need to add following credentials: \nTracking ID: {post.tracking_id} \nCode: {post.passcode}'
                    recepient = post.accused_email
                    send_mail(subject, 
                    message, EMAIL_HOST_USER, [recepient], fail_silently = False)

                subject = 'Case assigned'
                message = f'Hello {iodetails.user.first_name} {iodetails.user.last_name} \n\nA Case has been assigned to you! \nPlease check your Einvestigate Profile to check the details. \n\nRegards Einvestigate'
                recepient = iodetails.user.email 
                send_mail(subject, 
                message, EMAIL_HOST_USER, [recepient], fail_silently = False)

                context = {
                    'case' : post,
                    'temp_io_username': temp_io_username
                }
                return render(request, 'addcases/caseadded.html', context)  

            else:
                return render(request,'addcases/casenotadded.html')

    

    else:
        DISTRICT_CHOICES=['Select district','Ahmednagar','Akola','Amravati',
        'Aurangabad','Beed','Bhandara','Buldhana',
        'Chandrapur','Dhule','Gadchiroli','Gondia','Hingoli',
         'Jalgaon','Jalna','Kolhapur','Latur','Mumbai City',
         'Mumbai Suburban','Nagpur','Nanded','Nandurbar','Nashik',
         'Osmanabad','Palghar','Parbhani','Pune','Raigad','Ratnagiri',
         'Sangli','Satara','Sindhudurg','Solapur','Thane','Wardha','Washim','Yavatmal']
        context={
            'DISTRICT_CHOICES':DISTRICT_CHOICES,
        }
        # DISTRICT_CHOICES={
        # 'Select district': 'Select district',
        # 'Ahmednagar': 'Ahmednagar',
        # 'Akola':'Akola',
        # 'Amravati':'Amravati',
        # 'Aurangabad':'Aurangabad',
        # 'Beed':'Beed',
        # 'Bhandara':'Bhandara',
        # 'Buldhana':'Buldhana',
        # 'Chandrapur': 'Chandrapur',
        # 'Dhule':'Dhule',
        # 'Gadchiroli':'Gadchiroli',
        # 'Gondia':'Gondia',
        # 'Hingoli':'Hingoli',
        # 'Jalgaon':'Jalgaon',
        # 'Jalna':'Jalna',
        # 'Kolhapur': 'Kolhapur',
        # 'Latur':'Latur',
        # 'Mumbai City':'Mumbai City',
        # 'Mumbai Suburban':'Mumbai Suburban',
        # 'Nagpur':'Nagpur',
        # 'Nanded':'Nanded',
        # 'Nandurbar':'Nandurbar',
        # 'Nashik':'Nashik',
        # 'Osmanabad':'Osmanabad',
        # 'Palghar':'Palghar',
        # 'Parbhani':'Parbhani',
        # 'Pune':'Pune',
        # 'Raigad':'Raigad',
        # 'Ratnagiri':'Ratnagiri',
        # 'Sangli':'Sangli',
        # 'Satara':'Satara',
        # 'Sindhudurg':'Sindhudurg',
        # 'Solapur':'Solapur',
        # 'Thane':'Thane',
        # 'Wardha':'Wardha',
        # 'Washim':'Washim',
        # 'Yavatmal':'Yavatmal',
        
        # }
        return render(request,'addcases/addcase.html',context)
        



def caseadded(request, context):
    # last_case_added = {
    #     'post' : 
    # }
    return render(request, 'addcases/caseadded.html', context)

def casenotadded(request):
    return redirect('addcase')









