from django.db import models
from addcases.models import Case

class CriminalRecord(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Not Specified','Not Specified'),
    )
    
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    criminal_id = models.CharField(max_length=15, primary_key=True)
    criminal_firstname = models.CharField(max_length = 100, default='')
    criminal_lastname = models.CharField(max_length = 100, default='')
    birthdate = models.DateField(null=True, blank=True)
    no_of_crimes=models.PositiveSmallIntegerField(default=1)
    
    
class CriminalCase(models.Model):
    criminal_id = models.ForeignKey(CriminalRecord, on_delete = models.CASCADE, default='',related_name='crimcase')
    case_id = models.ForeignKey(Case, on_delete = models.CASCADE, default='')
    
    crime_description = models.TextField()
    sentence_status = models.TextField(max_length = 500)
    crime_punishment = models.TextField()



