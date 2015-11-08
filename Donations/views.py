from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
from .forms import RegistrationForm, LoginForm
import pdb
from Donations.models import User
from django.http import HttpResponseRedirect

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
		
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		for i in User.objects.all(): 
			if i.email == str(email): 
				if i.password == str(password):
					request.session['email'] = str(email)
					context = {
						"title": "Login successful"
					}
					return HttpResponseRedirect("/home/")
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
