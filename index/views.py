from django.shortcuts import render
from .models import destinations

# Create your views here.
def index(request):
    dests = destinations.objects.all()
    
    return render (request,'index.html', {'dests':dests})



    

    
 