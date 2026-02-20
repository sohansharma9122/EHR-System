from django import forms
from .models import Laboratory_test

class testForm(forms.ModelForm):
    class Meta:
        model= Laboratory_test
        fields= ['test_name','test_Price']
