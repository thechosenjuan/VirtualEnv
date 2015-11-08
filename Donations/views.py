from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
from .forms import RegistrationForm, LoginForm
import pdb
from Donations.models import User, Faq
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
		
		userEmail = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		try:
			user=User.objects.get(email=userEmail)
			if password == user.password:
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
	FAQ = Faq.objects.all()
	context = {
		"FAQ": FAQ,
	}
	return render(request, "Donations/faq.html", context)

