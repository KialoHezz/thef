from django.shortcuts import render
from .models import Business

# Create your views here.
def home(request):
    context = {
        "business": Business.objects.all(),
    }
    return render(request, 'home/home.html',context)

def business_search(request):
    if 'search_business' in request.GET and request.GET['search_business']:
        search_term = request.GET.get('search_business')
        searched_business = Business.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'home/business_search.html',{"message":message,"business": searched_business})
    else:
        message = "Your haven't search for any business"

    return render(request, 'home/business_search.html')
