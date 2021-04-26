from django.db import models
from django.utils import timezone
from core.models import Profile
timezone.localtime()

# class user(models.Model):
#     user_id = models.CharField(max_length=15, primary_key=True)
#     user_name = models.CharField(max_length=30)
    

class Case(models.Model):
    DISTRICT_CHOICES=(
        ('Select district', 'Select district'),
        ('Ahmednagar', 'Ahmednagar'),
        ('Akola', 'Akola'),
        ('Amravati','Amravati'),
        ('Aurangabad','Aurangabad'),
        ('Beed','Beed'),
        ('Bhandara','Bhandara'),
        ('Buldhana','Buldhana'),
        ('Chandrapur', 'Chandrapur'),
        ('Dhule','Dhule'),
        ('Gadchiroli','Gadchiroli'),
        ('Gondia','Gondia'),
        ('Hingoli','Hingoli'),
        ('Jalgaon','Jalgaon'),
        ('Jalna','Jalna'),
        ('Kolhapur', 'Kolhapur'),
        ('Latur', 'Latur'),
        ('Mumbai City','Mumbai City'),
        ('Mumbai Suburban','Mumbai Suburban'),
        ('Nagpur','Nagpur'),
        ('Nanded','Nanded'),
        ('Nandurbar','Nandurbar'),
        ('Nashik','Nashik'),
        ('Osmanabad','Osmanabad'),
        ('Palghar','Palghar'),
        ('Parbhani','Parbhani'),
        ('Pune','Pune'),
        ('Raigad','Raigad'),
        ('Ratnagiri','Ratnagiri'),
        ('Sangli','Sangli'),
        ('Satara','Satara'),
        ('Sindhudurg','Sindhudurg'),
        ('Solapur','Solapur'),
        ('Thane','Thane'),
        ('Wardha','Wardha'),
        ('Washim','Washim'),
        ('Yavatmal','Yavatmal'),
        
    )
    CATEGORY = (
        ('Robbery', 'Robbery'),
        ('Cyber-crime', 'Cyber-crime'),
        ('Domestic violence','Domestic violence'),
        ('Sexual Assault','Sexual Assault'),
        ('Child Abuse','Child Abuse'),
        ('Terrorism','Terrorism'),
        ('Violent Crime','Violent Crime'),
        ('Corruption','Corruption'),
        ('Poaching','Poaching'),
    )
    case_id = models.CharField(max_length=15, primary_key=True)
    case_dsp_id = models.CharField(max_length=15, default='')
    case_category = models.CharField(max_length=100,choices=CATEGORY,default='')
    case_description = models.TextField()
    crime_location = models.CharField(max_length=100)
    crime_district=models.CharField(max_length=30, choices=DISTRICT_CHOICES,default='')
    crime_date = models.DateField(max_length=10)
    complainant_name = models.CharField(max_length = 100, default='')
    complainant_contact = models.CharField(max_length=10, blank=True)
    complainant_email = models.EmailField(max_length=50, default='')
    accused_name = models.CharField(max_length = 100, default='')
    accused_contact = models.CharField(max_length=10, blank=True)
    accused_email = models.EmailField(max_length=50, default='')
    case_io = models.ForeignKey(Profile, on_delete = models.CASCADE, default='')
    
    case_added_date = models.DateTimeField(default=timezone.now)
    #tracking_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    tracking_id = models.CharField(unique=True, max_length=40, default='')
    passcode = models.CharField(max_length=8, unique=True, default='')



    # case_id=models.CharField(primary_key=True,max_length=15)
    # victim_name=models.CharField(max_length=255)
    # io_name=models.CharField(max_length=70)
    # io_id=models.CharField(max_length=15)
    # crime_date=models.DateTimeField(blank=True)
    # category=models.CharField(max_length=70)
    # victim_id=models.CharField(max_length=15)
    # crime_loc=models.CharField(max_length=255)