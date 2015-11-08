from django.contrib import admin

# Register your models here.
from .forms import RegistrationForm
from .models import User, Faq, Product, Project

class RegistrationAdmin(admin.ModelAdmin):
	list_display = ["full_name", "email", "password", "timestamp", "updated"]
	form = RegistrationForm

admin.site.register(User, RegistrationAdmin)

class FaqAdmin(admin.ModelAdmin):
	list_display = ["question", "answer", "timestamp", "updated"]

admin.site.register(Faq, FaqAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ["name", "price", "quantity", "description", "picture"]

admin.site.register(Product, ProductAdmin)

class ProjectAdmin(admin.ModelAdmin):
	list_display = ["name", "description", "location", "picture"]

admin.site.register(Project, ProjectAdmin)

