from django.contrib import admin

# Register your models here.
from .models import patientprofile_master,Doctor_Appointment,PatientTestReport
admin.site.register(patientprofile_master)
admin.site.register(Doctor_Appointment)
admin.site.register(PatientTestReport)