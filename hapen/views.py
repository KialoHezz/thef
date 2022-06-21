from django.shortcuts import render, redirect
from .models import Business, Contacts, NeighbourHood, User
from django.contrib.auth.decorators import login_required
from .forms import BusinessForm, ContactsForm, NeighbourHoodForm, UserForm, PostsForm

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
    contacts = Contacts.get_by_neighbourhood(id)
    current_user = request.user

    if request.method == 'POST':
  
        form = PostsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.neighbourhood = neighbourhood
            profiles = current_user.user_set.values()

            for profile in profiles:
                post.profile_id = profile['id']
                form.save()
        return redirect('neighbourhood', neighbourhood.id)
    else:

        form = PostsForm()

    return render(request, 'home/neighbourhood.html', {'form':form, 'neighbourhood': neighbourhood, "id": id,'contacts':contacts})


@login_required(login_url='/accounts/login/')
def new_neighbourhood(request):
    current_user = request.user

    if request.method == 'POST':

        form = NeighbourHoodForm(request.POST, request.FILES)

        if form.is_valid():

            upload = form.save(commit=False)
            upload.editor = current_user

            upload.save()

        return redirect('home')
    else:
        form = NeighbourHoodForm()

    return render(request, 'home/new_neighbourhood.html', {'form': form, })


@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user

    if request.method == 'POST':

        form = UserForm(request.POST, request.FILES)

        if form.is_valid():

            upload = form.save(commit=False)
            upload.editor = current_user

            upload.save()

        return redirect('home')
    else:
        form = UserForm()

    return render(request, 'profile/new_profile.html', {'form': form, })

