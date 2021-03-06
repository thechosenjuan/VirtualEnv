from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.conf import settings
from .forms import RegistrationForm, LoginForm
import pdb
from Donations.models import User, Faq, Project, Product, Cart, ItemSold
from django.http import HttpResponseRedirect
from django.http import Http404




# Create your views here.
def home(request):
	if 'email' not in request.session:
		return HttpResponseRedirect("/login/")
	return render_to_response("Donations/home.html")


def login(request):
	title = "Welcome"
	form = LoginForm(request.POST or None)
	#if request.user.is_authenticated():
	#	title = "My title %s" %(request.user)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		#form.save()

		userEmail = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		try:
			user=User.objects.get(email=userEmail)
			if password == user.password:
				request.session['email'] = userEmail
				return HttpResponseRedirect("/home/")
			else:
				context = {
					"title": "Wrong password",
					"form": form
				}
		except User.DoesNotExist:
			context = {
				"title": "User not found",
				"form": form
			}

	return render(request, "Donations/login.html", context)

def registration(request):
	title = "Registration"
	form = RegistrationForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		email = form.cleaned_data.get("email")
		instance = form.save(commit="False")
		context = {
			"title": "Registration complete"
		}
		request.session['email'] = str(email)
		return HttpResponseRedirect("/home/")

	return render(request, "Donations/registration.html", context)


def logout(request):
	if 'email' not in request.session:
		return HttpResponseRedirect("/login/")
	del request.session['email']
	return HttpResponseRedirect("/login/")

def faq(request):
	if 'email' not in request.session:
		return HttpResponseRedirect("/login/")

	FAQ = Faq.objects.all()
	context = {
		"FAQ": FAQ,
	}
	return render(request, "Donations/faq.html", context)

def projects(request):
	if 'email' not in request.session:
		return HttpResponseRedirect("/login/")

	project = Project.objects.all()
	context = {
		"Project":project
	}
	return render(request, "Donations/projects.html", context)

def projectDetails(request, Project_id):
	if 'email' not in request.session:
		return HttpResponseRedirect("/login/")

	try:
		project = Project.objects.get(pk=Project_id)
		products = Product.objects.all()
	except Project.DoesNotExist:
		raise Http404("Project does not exist")
	context = {
		'Project': project,
		'Products' : products,
		'Project_id' : Project_id
		}

	return render(request, 'Donations/detail.html', context)

def add_item_to_cart(request):
	if 'email' not in request.session:
		return HttpResponseRedirect("/login/")

	if request.GET.get('quantity'):
		product_id = request.GET['product']
		product_toAdd = Product.objects.get(pk=product_id)

		project_id = request.GET['Project_id']
		project_toAdd = Project.objects.get(pk=project_id)

		quantity_toAdd = request.GET['quantity']

		message = "carrito actualizado!"
		user_toAdd = User.objects.get(email = str(request.session['email']))

		existItemInCart = 0
		for i in Cart.objects.all():
			if i.user.full_name == user_toAdd.full_name and i.product.name == product_toAdd.name and i.project.name == project_toAdd.name:
				existItemInCart = i
				existItemInCart.quantity = int(existItemInCart.quantity) + int(quantity_toAdd)
				existItemInCart.save()
				return redirect("Donations.views.projectDetails", Project_id=project_id)

		product_toAddCart = Cart(user = user_toAdd, project = project_toAdd, product = product_toAdd, quantity = int(quantity_toAdd))
		product_toAddCart.save()
	else:
		message = 'You submitted nothing!'
	return redirect("Donations.views.projectDetails", Project_id=project_id)

def remove_item_from_cart(request):
	if 'email' not in request.session:
		return HttpResponseRedirect("/login/")

	car_id = request.GET['cartItem']
	item = Cart.objects.get(pk=car_id)
	item.delete()
	return HttpResponseRedirect("/cart/")

def cart(request):
	if 'email' not in request.session:
		return HttpResponseRedirect("/login/")

	items = []
	for i in Cart.objects.all():
		if i.user.email == request.session['email']:
			items.append(i)
	total=0
	for i in items:
		total=total+i.quantity*i.product.price
	context = {
		"Cart": items,
		"total": total
	}
	return render(request, "Donations/cart.html", context)

def about_us(request):
	if 'email' not in request.session:
		return HttpResponseRedirect("/login/")

	return render_to_response("Donations/about_us.html")

def contact(request):
	if 'email' not in request.session:
		return HttpResponseRedirect("/login/")
	context = {
		"Contact": "Contact"
	}
	return render(request, "Donations/contact.html", context)

def checkout(request):
	if 'email' not in request.session:
		return HttpResponseRedirect("/login/")
	return render_to_response("Donations/checkout.html")

def itemsBought(request):
	if 'email' not in request.session:
		return HttpResponseRedirect("/login/")
	user = request.session['email']

	items = []
	toDelete = []
	#get elements with the active user
	for i in Cart.objects.all():
		if i.user.email == request.session['email']:
			items.append(i)
			toDelete.append(i.id)
	
	#itemsBought added to the ItemSold
	for i,x in zip(items,toDelete):
		product_toAddSold = ItemSold(user = i.user, project = i.project, product = i.product, quantity = i.quantity)
		product_toAddSold.save()
		Cart.objects.get(pk=x).delete()

	return HttpResponseRedirect("/home/")
