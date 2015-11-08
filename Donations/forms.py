from django import forms

from .models import User


class RegistrationForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['full_name', 'email', 'password']
		
	def clean_email(self):
		email = self.cleaned_data.get('email')
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name

	def clean_password(self):
		password = self.cleaned_data.get('password')
		return password