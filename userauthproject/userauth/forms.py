from django import forms
from django.contrib.auth.models import User

from userauth.models import UserProfile

class UserForm(forms.ModelForm):
	username = forms.CharField(help_text="Please enter username")
	email = forms.CharField(help_text="Please enter email")
	password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter password")
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
	website = forms.URLField(help_text="Please enter website", required=False)
	opinion = forms.CharField(help_text="Your opinion on shoes", required=False)
	
	class Meta:
		model = UserProfile
		fields = ['website', 'opinion']