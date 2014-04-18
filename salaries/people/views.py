from django.shortcuts import render
from django.http import HttpResponse
from people.models import Person
	
    
def home(request):
    names = Person.objects.order_by('name')
    return render(request, 'index.html', {'names': names})
    
def personDetail(request, slug):
    name = Person.objects.get(name_slug=slug)
    salary = Person.objects.get(name_slug=slug).salary 
    return render(request, 'persondetail.html', {'name': name, 'salary': salary})    