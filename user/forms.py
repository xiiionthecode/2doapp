from django import forms
from django.forms import widgets
from .models import *

class Userinfo_Form(forms.ModelForm):
    class Meta:
        model = user_info
        fields = [
            'name',
            'password',
            'email',


        ]
        widgets = {
            'name': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' Enter username ', 'type':'text'}),
            'password': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' Enter password ', 'type':'password'}),
            'email': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' Enter email ', 'type':'email'}),
        }
