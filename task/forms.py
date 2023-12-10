from django import forms
from django.forms import widgets
from .models import *

PRIORITY_CHOICES = [
    ('low', 3),
    ('medium', 2),
    ('high', 1),
]

STATUS_CHOICES = [
    ('todo', 'To Do'),
    ('in_progress', 'In Progress'),
    ('done', 'Done'),
]

class Task_Form(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'priority',
            'status',


        ]
        widgets = {
            'title': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' Enter title ', 'type':'text'}),
            'description': forms.Textarea(attrs={ 'class':'form-control', 'placeholder': ' Enter description ',}),
            'priority': forms.Select(attrs={ 'class':'form-control'}),
            'status': forms.Select(attrs={ 'class':'form-control'}),
        }
