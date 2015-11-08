from django.contrib import admin

# Register your models here.
from .forms import RegistrationForm
from .models import User

class RegistrationAdmin(admin.ModelAdmin):
	list_display = ["full_name", "email", "password", "timestamp", "updated"]
	form = RegistrationForm

admin.site.register(User, RegistrationAdmin)

