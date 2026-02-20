from django.contrib import admin

# Register your models here.
from .models import Prescription,doctorprofile_master
admin.site.register(Prescription)
admin.site.register(doctorprofile_master)

