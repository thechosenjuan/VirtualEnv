from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
from .forms import RegistrationForm

# Create your views here.
def home(request):
    return render_to_response("Donations/home.html")

def login(request):
	title = "Welcome"
	form = SignUpForm(request.POST or None)
	#if request.user.is_authenticated():
	#	title = "My title %s" %(request.user)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		#form.save()
		instance = form.save(commit="False")
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full_name"
		instance.full_name = full_name
		context = {
			"title": "Thank you"
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
