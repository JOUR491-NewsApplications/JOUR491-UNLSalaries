from django.shortcuts import render
from django.http import HttpResponse
from people.models import Person
from haystack.query import SearchQuerySet
from forms import NotesSearchForm
	
    
def home(request):
    names = Person.objects.order_by('name')
    return render(request, 'index.html', {'names': names})
    
def personDetail(request, slug):
    name = Person.objects.filter(name_slug=slug)
    return render(request, 'persondetail.html', {'name': name })
    

    
def root(request):
    """
    Search > Root
    """

    form = NotesSearchForm(request.GET)

    results = form.search()

    return render(request, 'search/search.html', {
        'search_query' : search_query,
        'notes' : results,
    })    
    
    