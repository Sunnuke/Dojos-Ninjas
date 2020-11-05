from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    print(request.session['count'])
    context = {
        'Dojos': Dojo.objects.all(),
        'count': Ninja.objects.all()
    }
    return render(request, 'index.html', context)

def ninja(request):
    new_id = int(request.POST['dojo'])
    Ninja.objects.create(
        dojo=Dojo.objects.get(id=new_id),
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name']
    )
    return redirect('/')

def dojo(request):
    Dojo.objects.create(
        loc_name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state']
    )
    return redirect('/')

def deleted(request):
    deleted = Dojo.objects.get(
        id=int(request.POST['deleted'])
    )
    deleted.delete()
    return redirect('/')
