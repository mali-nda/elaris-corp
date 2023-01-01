from django import forms

from .models import *

class ContactUsForm(forms.ModelForm):
	first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
		'placeholder': 'First Name'
		}))
	last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
		'placeholder': 'Last Name'
		}))
	email = forms.EmailField(widget=forms.TextInput(attrs={
		'placeholder': 'Email'
		}))

	class Meta:
		model = ContactUs

		fields = [
			'first_name',
			'last_name',
			'email',
			'details',
		]
