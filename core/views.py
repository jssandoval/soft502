from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# Create your views here.


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'core/home.html'
    login_url = '/admin'