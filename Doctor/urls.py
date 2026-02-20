from django.urls import path
from Doctor.views import Dhome,Pviewdata,display_appointment,approve_appointment,cancel_appointment,viewdetails,Doctorprofile

urlpatterns = [
    path('',Dhome,name="Dhome"),
    path('Pviewdata/',Pviewdata,name='Pviewdata'),
    path('display_appointment/', display_appointment, name="display_appointment"),
    path('approve_appointment/',approve_appointment,name="approve_appointment"),
    path('cencel/', cancel_appointment,name='cancel_appointment'),
    path('viewdetails/', viewdetails, name='viewdetails'),
    path('doctorprofile/', Doctorprofile, name='doctorprofile'),
  
]
