from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from . import models


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, 'destinations.html', {'destinations': all_destinations})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def reset_password(request):
    return render(request, 'reset_password.html')

class DestinationDetailView(generic.DetailView):
    model = models.Destination
    template_name = 'destinations_detail.html'
    context_object_name = 'destination'

class CruiseDetailView(generic.DetailView):
    model = models.Cruise
    template_name='cruise_detail.html'
    context_object_data = 'cruise'

# class InfoRequestCreate(SuccessMessageMixin, generic.CreateView):
#     model = models.InfoRequest
#     template_name = 'info_request_create.html'
#     fields = ['name', 'email', 'cruise', 'notes']
#     success_url = reverse_lazy('index')
#     success_message = f"Thank you, {name}! We will email you when we have more information about {cruise}"