from django.shortcuts import render
from .models import Business

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def business_search(request):
    if 'search_business' in request.GET and request.GET['search_business']:
        search_term = request.GET.get('search_business')
        searched_business = Business.search_by_title(search_term)
    return render(request, 'home/business_search.html')
