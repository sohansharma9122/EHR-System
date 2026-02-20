from django.urls import path
from Staff.views import Shome,pd_viewdata,add_test

urlpatterns = [
    path('',Shome,name="Shome"),
    path('pd_viewdata/', pd_viewdata, name="pd_viewdata"),
    path('add_test/', add_test, name="add_test"),
    
    
]
