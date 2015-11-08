from django.contrib import admin

# Register your models here.
from .forms import SignUpForm, RegistrationForm
from .models import SignUp,Registration


class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = SignUpForm

admin.site.register(SignUp, SignUpAdmin)

class RegistrationAdmin(admin.ModelAdmin):
	list_display = ["full_name", "email", "password", "timestamp", "updated"]
	form = RegistrationForm

admin.site.register(Registration, RegistrationAdmin)

