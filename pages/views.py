from django.shortcuts import render
from django.views.generic import TemplateView
from . import views


class HomePageView(TemplateView):
    template_name = 'home.html'

def contact(request):
    return render(request, 'contact.html', {})


def booking(request):
    context = {}
    template_name = 'booking.html'
    return render(request, 'booking.html', {})

def about(request):
    context = {}
    template_name = 'about.html'
    return render(request, 'about.html', {})

