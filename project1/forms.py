from django.forms import ModelForm
from .models import OnlineComplaint

class OnlineComplaintForm(ModelForm):
    class Meta:
        model = OnlineComplaint
        fields = ['complainant_name', 'complainant_contact', 'complainant_email', 'complainant_address', 'complaint', 'crime_district', 'crime_location']