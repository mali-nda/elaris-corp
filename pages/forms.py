from django import forms

from .models import *

class JobDetailForm(forms.ModelForm):
    applicant_name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={
		'placeholder': 'Full Name'
		}))
    applicant_phone = forms.CharField(label='Phone No', widget=forms.TextInput(attrs={
		'placeholder': 'Phone No'
		}))
    applicant_email = forms.EmailField(widget=forms.TextInput(attrs={
		'placeholder': 'Email'
		}))
    resume = forms.FileField()
	
    class Meta:
        model = Application
        fields = [
            'applicant_name',
            'applicant_phone',
            'applicant_email',
            'resume',
        ]