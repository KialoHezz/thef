from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<user>', views.profile,name = 'profile'),

]