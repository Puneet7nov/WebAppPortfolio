from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth import authenticate
from .models import SignUp

class SignUpForm(UserCreationForm):
    phonenumber = PhoneNumberField(
    	widget=forms.TextInput(
    		attrs={'rows': 1, 'placeholder': 'Enter 10 digit mobile number with Country Code'}
    		), 
    		max_length=14,
    		help_text='Country code is required. e.g. +919900220022'
    	)
    email = forms.CharField(
    	max_length=254, 
    	required=True, 
    	widget=forms.EmailInput()
    	)
    firstname = forms.CharField(
    	max_length=50, 
    	required=True, 
    	widget=forms.Textarea(
    		attrs={'rows': 1, 'placeholder': 'Enter Your First Name'}
    		),
    	)
    lastname = forms.CharField(
    	max_length=50, 
    	required=True, 
    	widget=forms.Textarea(
    		attrs={'rows': 1, 'placeholder': 'Enter Your Surname Name'}
    		),
    	)


    class Meta:
    #    model = User
    #    fields = ['firstname', 'lastname', 'email', 'phonenumber', 'password1', 'password2']
        model = SignUp
        fields = ['firstname', 'lastname', 'email', 'phonenumber', 'password1', 'password2']


class AuthenticationForm(forms.Form):
    email = forms.CharField(
    	max_length=254, 
    	required=True, 
    	widget=forms.EmailInput()
    	)
    password = forms.CharField(widget=forms.PasswordInput)