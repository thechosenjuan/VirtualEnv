from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
from .forms import RegistrationForm, LoginForm
import pdb
from Donations.models import User

# Create your views here.
def home(request):
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
		
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		#pdb.set_trace()
		for i in User.objects.all(): 
			if i.email == str(email): 
				if i.password == str(password):
					context = {
						"title": "Login successful"
					}
					return render(request, "Donations/home.html", context)
				else:
					context = {
						"title": "Wrong password"
					}
			else:

				context = {
					"title": "User not found"
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
		instance = form.save(commit="False")
		context = {
			"title": "Registration complete"
		}

	return render(request, "Donations/registration.html", context)
