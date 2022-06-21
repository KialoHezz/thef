from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<editor>', views.profile,name = 'profile'),
    path('neighbourhood/<id>', views.neighbourhood,name = 'neighbourhood'),
    path('new/neighbourhood/', views.new_neighbourhood,name = 'new_neighbourhood'),
    path('new/business/', views.new_business,name = 'new_business'),
    path('profile/new/', views.new_profile,name = 'new_profile'),



]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
