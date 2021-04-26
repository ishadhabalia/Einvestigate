from django.contrib import admin
from .models import CriminalRecord
from .models import CriminalCase

admin.site.register(CriminalRecord)
admin.site.register(CriminalCase)
# Register your models here.
