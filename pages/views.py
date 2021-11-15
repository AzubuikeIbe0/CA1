from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(LoginRequiredMixin, UserPassesTestMixin,TemplateView):
    template_name = 'home.html'

    def test_func(self):
        return self.request.user.profile

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

