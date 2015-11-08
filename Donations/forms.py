from django import forms

from .models import SignUp, Registration


class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name','email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = Registration
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