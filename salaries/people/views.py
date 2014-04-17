from django.shortcuts import render
from django.http import HttpResponse
from people.models import Person
	
    
def home(request):
    names = Person.objects.order_by('name')
    return render(request, 'index.html', {'names': names})
    