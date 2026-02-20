from django.urls import path
from Patient.views import Phome,pdviewdata,patientprofile,patientviewprofile,take_appointment,success,patient_dashboard,viewlabtest,testreport,applytest,payment_success,download_report_pdf

urlpatterns = [
    path('',Phome,name="Phome"),
    path("pdviewdata/", pdviewdata, name="pdviewdata"),
    path('patientprofile/',patientprofile, name='patientprofile'),
    path('patientviewprofile/',patientviewprofile, name='patientviewprofile'),
    path('success/',success, name="success"),
    path('take_appointment/',take_appointment, name="take_appointment"),
    path('patient_dashboard/',patient_dashboard, name="patient_dashboard"),
    path('viewlabtest/',viewlabtest, name="viewlabtest"),
    path('testreport/',testreport,name="testreport"),
    path('applytest/',applytest, name="applytest"),
    path("payment-success/",payment_success, name="payment_success"),
    path("download-report/<int:report_id>/", download_report_pdf, name="download_report_pdf"),


]
