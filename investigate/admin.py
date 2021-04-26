from django.contrib import admin
from .models import TextEvidence
from .models import FileEvidence
from .models import Suspects
from .models import Leads

# Register your models here.
admin.site.register(TextEvidence)
admin.site.register(FileEvidence)
admin.site.register(Suspects)
admin.site.register(Leads)