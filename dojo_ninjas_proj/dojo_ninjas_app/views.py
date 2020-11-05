from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    context = {
        'Dojos': Dojo.objects.all(),
        # 'ninjas': Ninja.objects.all()
    }
    return render(request, 'index.html', context)

def ninja(request):

    # Ninja.objects.create(
    return redirect('/')

def dojo(request):
    
    # Dojo.objects.create(
    return redirect('/')