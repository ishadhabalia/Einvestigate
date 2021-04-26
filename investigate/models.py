from django.db import models
from addcases.models import Case
from django.utils import timezone
timezone.localtime()

# Create your models here.

class TextEvidence(models.Model):
    case_id = models.ForeignKey(Case, on_delete = models.CASCADE, default='')
    edit_id = models.CharField(max_length = 3)
    edit_title = models.CharField(max_length = 500)
    edit_content = models.TextField(max_length = 5000)
    edit_datetime = models.DateTimeField(default=timezone.now)

class FileEvidence(models.Model):
    case_id = models.ForeignKey(Case, on_delete = models.CASCADE, default='')
    edit_id = models.CharField(max_length = 3)
    edit_title = models.CharField(max_length = 500)
    file_name = models.CharField(max_length=500)
    file_path = models.FileField(upload_to='files/', null=True, verbose_name="")
    edit_datetime = models.DateTimeField(default=timezone.now)  
    
    def __str__(self):        
        # return self.file_name
        return self.file_name + ": " + str(self.file_path)
  

    # def __str__(self):
    #     return self.file_name + ": " + str(self.file_path)

class Suspects(models.Model):
    case_id = models.ForeignKey(Case, on_delete = models.CASCADE, default='')
    edit_id = models.CharField(max_length = 3)
    suspect_name = models.CharField(max_length = 100)
    suspect_contact = models.CharField(max_length = 10)
    suspect_address = models.TextField (max_length = 300)
    suspect_reason = models.TextField(max_length = 5000)
    edit_datetime = models.DateTimeField(default=timezone.now) 


class Leads(models.Model):
    case_id = models.ForeignKey(Case, on_delete = models.CASCADE, default='')
    edit_id = models.CharField(max_length = 3)
    edit_title = models.CharField(max_length = 100)
    edit_content = models.TextField(max_length = 5000)
    edit_datetime = models.DateTimeField(default=timezone.now)