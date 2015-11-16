from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.conf import settings
from .forms import RegistrationForm, LoginForm
import pdb
from Donations.models import User, Faq, Project, Product, Cart
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

def cart(request):
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
