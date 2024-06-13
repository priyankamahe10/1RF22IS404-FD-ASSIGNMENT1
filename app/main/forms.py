from django import forms
from .models import Customer,Student
class inputform2(forms.ModelForm):
    class Meta:
        model=Student
        fields=['usn','name']

class inputform(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','aadhar','pincode']


class inputform1(forms.Form):
    n = forms.IntegerField(max_value=10, min_value=1, label="Enter a number")    