from django.urls import path
from Contact.views import Contact

urlpatterns = [
    path('',Contact, name="contact")
]