from django.urls import path
from EhrAdmin.views import Ahome,aviewdata,update,adminprofile,adminviewprofile

urlpatterns = [
    path('',Ahome,name="Ahome"),
    path('aviewdata/',aviewdata, name='aviewdata'),
    path('update/',update, name='update'),
    path('adminprofile/',adminprofile, name='adminprofile'),
    path('adminviewprofile/',adminviewprofile, name='adminviewprofile'),

    
]
