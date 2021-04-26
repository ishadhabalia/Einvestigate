import django_filters
from django_filters import CharFilter
from django_filters import DateFilter,ModelChoiceFilter


from crimerec.models import CriminalRecord, CriminalCase
from addcases.models import Case
from django import forms

class CriminalRecordFilter(django_filters.FilterSet):
    criminal_firstname = CharFilter(field_name='criminal_firstname', lookup_expr='icontains',label='First name') 
    criminal_lastname = CharFilter(field_name='criminal_lastname', lookup_expr='icontains',label='Last name')
    crimcase__criminal_id = CharFilter(field_name='crimcase__criminal_id',label='Criminal ID')
    crimcase__case_id = CharFilter(field_name='crimcase__case_id',label='Case ID')
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

    crime_district = django_filters.ChoiceFilter(
        method='district_filter', label='District',
        choices = DISTRICT_CHOICES     
    ) 
    case_category = django_filters.ChoiceFilter(
        method='category_filter', label='Category',
        choices = CATEGORY    
    )

    class Meta:
        model=CriminalRecord
        fields=['gender']
        # child_model=Case
        # child_fields=['case_category']
        # fields=['crime_category','crimedate','crime_district']

    def district_filter(self,queryset, name, value):
        case = Case.objects.filter(crime_district=value)
        criminalcase = []
        for c in case:
            cc = CriminalCase.objects.filter(case_id = c)
            for i in cc:
                criminalcase.append(i)

        crimerecord_ids = []
        for c in criminalcase:
            crimerecord_ids.append(c.criminal_id.criminal_id)
        
        qs = CriminalRecord.objects.filter(criminal_id__in = crimerecord_ids)
        qs = queryset & qs
        return qs

    def category_filter(self,queryset, name, value):
        case = Case.objects.filter(case_category=value)
        
        criminalcase = []
        for c in case:
            cc = CriminalCase.objects.filter(case_id = c)
            for i in cc:
                # if CriminalCase.objects.filter(case_id = c).first() != None:
                # criminalcase.append(CriminalCase.objects.filter(case_id = c).first())
                criminalcase.append(i)

        crimerecord_ids = []
        for c in criminalcase:
            crimerecord_ids.append(c.criminal_id.criminal_id)
        
        qs = CriminalRecord.objects.filter(criminal_id__in = crimerecord_ids)
        qs = queryset & qs
        return qs
