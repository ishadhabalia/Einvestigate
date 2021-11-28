from django.db import models
from addcases.models import Case
from django.utils import timezone

class CaseStatus(models.Model):
    case_id = models.ForeignKey(Case, on_delete = models.CASCADE, default='')
    case_status_no = models.CharField(max_length = 3)
    status_title = models.CharField (max_length = 500, default='')
    status_content = models.TextField(max_length = 500)
    updated_datetime = models.DateTimeField(default=timezone.now) 

class OnlineComplaint(models.Model):
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
    complaint_id = models.AutoField(primary_key=True)
    complainant_name = models.CharField(max_length = 100, default='')
    complainant_contact = models.CharField(max_length=10, blank=True)
    complainant_email = models.EmailField(max_length=50, default='')
    complainant_address = models.TextField()
    complaint = models.TextField()
    crime_district=models.CharField(max_length=30, choices=DISTRICT_CHOICES,default='')
    crime_location = models.CharField(max_length=100)
