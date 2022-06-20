from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<editor>', views.profile,name = 'profile'),
    path('neighbourhood/<id>', views.neighbourhood,name = 'neighbourhood'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
