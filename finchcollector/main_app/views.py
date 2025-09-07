from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch

# Create your views here.
# main_app/views.py


# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

# views.py

def finch_index(request):
    finchs = Finch.objects.all() 
    return render(request, 'finchs/index.html', {'finchs': finchs})

def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finchs/detail.html', {'finch': finch})
class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
class FinchUpdate(UpdateView):
    model = Finch
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finchs/'