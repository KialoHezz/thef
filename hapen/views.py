from django.shortcuts import render
from .models import Business, NeighbourHood, User

# Create your views here.
def home(request):
    business = Business.get_all()
    neighbourhood = NeighbourHood.get_all()

    return render(request, 'home/home.html',{'business': business, 'neighbourhood': neighbourhood})

def business_search(request):
    if 'search_business' in request.GET and request.GET['search_business']:
        search_term = request.GET.get('search_business')
        searched_business = Business.search_by_title(search_term)
    return render(request, 'home/business_search.html')


# @login_required(login_url='/accounts/login/')
def profile(request, editor):
    profile = User.get_by_user(editor)
    # projects = Projects.filter_by_user(user)
    # title = profile.user

    return render(request, 'profile/profile.html', {'profile': profile, "editor": editor})

def neighbourhood(request, id):
    neighbourhood = NeighbourHood.get_by_id(id)

    return render(request, 'home/neighbourhood.html', {'neighbourhood': neighbourhood, "id": id})
