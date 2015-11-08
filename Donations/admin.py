from django.contrib import admin

# Register your models here.
from .forms import RegistrationForm
from .models import User, Faq, Product, Project,  Cart
import pdb


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

class CartAdmin(admin.ModelAdmin):
	model = Cart
	list_display = ["get_user", "get_product", "quantity", "get_price"]

	def get_user(self, obj):
		return obj.user.full_name
	get_user.short_description = "Author Name"

	def get_product(self, obj):
		return obj.product.name
	get_product.short_description = "Product Name"

	def get_price(self, obj):
		return obj.product.price
	get_price.short_description = "Price"

admin.site.register(Cart, CartAdmin)



