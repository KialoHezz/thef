
from django.shortcuts import render, redirect
from .models import Business, Contacts, NeighbourHood, User,Posts
from django.contrib.auth.decorators import login_required
from .forms import BusinessForm, ContactsForm, NeighbourHoodForm, UserForm, PostsForm

# Create your views here.
def home(request):
    context = {
        "business" : Business.get_all(),
        "neighbourhood" : NeighbourHood.get_all(),
        "post":Posts.objects.all(),
    }
    
    return render(request, 'home/home.html',context)



def business_search(request):
    print("This")
    if 'business_search' in request.GET and request.GET['business_search']:
        print("This far")
        search_term = request.GET.get('business_search')
        business = Business.search_by_name(search_term)
        return render(request, 'home/business_search.html',{'business':business})
    else:
        message = 'We have not found your search term'
        return render(request, 'home/business_search.html', {'message': message})



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
            post.editor = current_user
            post.neighbourhood = neighbourhood
            profiles = current_user.user_set.values()

            for profile in profiles:
                post.profile_id = profile['id']
                form.save()
        return redirect('neighbourhood', neighbourhood.id)
    else:

        form = PostsForm()

    return render(request, 'home/neighbourhood.html', {'form':form, 'neighbourhood': neighbourhood, "id": id,'contacts':contacts})



@login_required(login_url='/login/')
def new_neighbourhood(request):
    current_user = request.user

    if request.method == 'POST':

        form = NeighbourHoodForm(request.POST, request.FILES)

        if form.is_valid():

            business = form.save(commit=False)
            business.editor = current_user
            business.neighbourhood = neighbourhood

            business.save()

        return redirect('home')
    else:
        form = NeighbourHoodForm()

    return render(request, 'home/new_neighbourhood.html', {'form': form, })


@login_required(login_url='/login/')
def new_business(request, id):
    neighbourhood = NeighbourHood.get_by_id(id)
    current_user = request.user

    if request.method == 'POST':

        form = BusinessForm(request.POST, request.FILES)

        if form.is_valid():

            upload = form.save(commit=False)
            upload.editor = current_user
            upload.neighbourhood = neighbourhood

            upload.save()

        return redirect('neighbourhood', neighbourhood.id)
    else:
        form = BusinessForm()

    return render(request, 'home/new_business.html', {'form': form, 'neighbourhood': neighbourhood,})

    
@login_required(login_url='/login/')
def new_contacts(request, id):
    neighbourhood = NeighbourHood.get_by_id(id)
    current_user = request.user

    if request.method == 'POST':

        form = ContactsForm(request.POST, request.FILES)

        if form.is_valid():

            upload = form.save(commit=False)
            upload.editor = current_user
            upload.neighbourhood = neighbourhood

            upload.save()

        return redirect('neighbourhood', neighbourhood.id)
    else:
        form = ContactsForm()

    return render(request, 'home/new_contacts.html', {'form': form, 'neighbourhood': neighbourhood,})


@login_required(login_url='/login/')

def new_profile(request):
    current_user = request.user

    if request.method == 'POST':

        form = UserForm(request.POST, request.FILES)

        if form.is_valid():

            upload = form.save(commit=False)
            upload.editor = current_user

            upload.save()
            neighbourhood= upload.Neighbourhood

        return redirect('neighbourhood' ,neighbourhood.id)
    else:
        form = UserForm()

    return render(request, 'profile/new_profile.html', {'form': form, })