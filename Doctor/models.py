from django.db import models
from  Register.models import Register_Master
from Patient.models import *
# Create your models here.



class Prescription(models.Model):
    pres_id = models.AutoField(primary_key=True)
    app_id = models.ForeignKey(Doctor_Appointment, on_delete=models.CASCADE)
    prescription_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription {self.pres_id} for Appointment {self.app_id}"

class doctorprofile_master(models.Model):
    email=models.ForeignKey(Register_Master , on_delete=models.CASCADE)
    Image=models.ImageField(upload_to="Image")
    Designation = models.CharField(max_length=100)
    Document=models.FileField(upload_to="Doc")