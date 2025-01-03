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

def cruises(request):
    all_cruises = models.Cruise.objects.all()
    return render(request, 'cruises.html', {'cruises': all_cruises})

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

class DestinationCreateView(generic.CreateView):
    model = models.Destination
    template_name = 'destinations_form.html'
    context_object_name = 'destination'

class DestinationUpdateView(generic.UpdateView):
    model = models.Destination
    template_name = 'destinations_form.html'
    context_object_name = 'destination'

class DestinationDeleteView(generic.DeleteView):
    model = models.Destination
    template_name = 'destinations_detail.html'
    context_object_name = 'destination'

class CruiseDetailView(generic.DetailView):
    model = models.Cruise
    template_name='cruise_detail.html'
    context_object_data = 'cruise'