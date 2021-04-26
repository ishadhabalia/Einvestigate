from django.db import models
from addcases.models import Case
from django.utils import timezone

class CaseStatus(models.Model):
    case_id = models.ForeignKey(Case, on_delete = models.CASCADE, default='')
    case_status_no = models.CharField(max_length = 3)
    status_title = models.CharField (max_length = 500, default='')
    status_content = models.TextField(max_length = 500)
    updated_datetime = models.DateTimeField(default=timezone.now) 
     


    
