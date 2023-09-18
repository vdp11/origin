

# Create your views here.
from django.shortcuts import render
from .models import BandMember

def home(request):
    return render(request, 'band/home.html')

def about(request):
    return render(request, 'band/about.html')

def contact(request):
    return render(request, 'band/contact.html')
