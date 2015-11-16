"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^home/$', 'Donations.views.home', name="home"),
    url(r'^login/$', 'Donations.views.login', name="login"),
    url(r'^logout/$', 'Donations.views.logout', name="logout"),
    url(r'^faq/$', 'Donations.views.faq', name="faq"),
    url(r'^about_us/$', 'Donations.views.about_us', name="about_us"),
    url(r'^cart/$', 'Donations.views.cart', name="cart"),
    url(r'^projects/$', 'Donations.views.projects', name="projects"),
    url(r'^projects/(?P<Project_id>[0-9]+)/$', 'Donations.views.projectDetails', name='projectDetails'),
    url(r'^registration/$', 'Donations.views.registration', name="registration"),
    url(r'^add_item_to_cart/$', 'Donations.views.add_item_to_cart', name="add_item_to_cart"),
    url(r'^remove_item_from_cart/$', 'Donations.views.remove_item_from_cart', name="remove_item_from_cart"),
    url(r'^admin/', include(admin.site.urls)),
]
