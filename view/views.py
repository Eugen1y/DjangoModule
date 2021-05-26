from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class Contacts(TemplateView):
    template_name = 'static/contacts.html'


class About(TemplateView):
    template_name = 'static/about.html'


class Home(TemplateView):
    template_name = 'static/home.html'
