from django.db import models
from Register.models import Register_Master
from datetime import date,time
from Staff.models import Laboratory_test
# Create your models here.

class PatientTestReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Register_Master, on_delete=models.CASCADE)
    tests = models.ManyToManyField(Laboratory_test)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    report_file = models.FileField(upload_to="reports/", blank=True, null=True)
    
    # New fields for payment
    is_paid = models.BooleanField(default=False)
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Report {self.report_id} - {self.patient.Name}"
    
class patientprofile_master(models.Model):
    email=models.ForeignKey(Register_Master,on_delete=models.CASCADE)
    Patient_id=models.AutoField(primary_key=True)
    Diseases=models.CharField(max_length=50, default="Unknown")
    Image=models.ImageField(upload_to="Image/")
    Document=models.FileField(upload_to="Doc/")



class Doctor_Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    doct_name = models.CharField(max_length=100)
    doct_contact = models.CharField(max_length=15)
    doct_email = models.ForeignKey(Register_Master,on_delete=models.CASCADE)
    p_name = models.CharField(max_length=100)
    p_mobile = models.CharField(max_length=15)
    p_address = models.TextField()
    p_gender = models.CharField(max_length=10)
    dob = models.DateField()
    p_disease = models.CharField(max_length=255)
    todaydate = models.DateField(auto_now=True)
    a_date = models.DateField(default=date.today)
    fromTime = models.TimeField(default=time(9, 0))
    totime = models.TimeField(default=time(17, 0))
    status=models.CharField(max_length=30,default='Pending')
    def __str__(self):
        return self.doct_name
