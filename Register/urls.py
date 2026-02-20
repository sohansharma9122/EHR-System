
from django.urls import path
from Register.views import Signup

urlpatterns = [
    path('',Signup, name="register")
]