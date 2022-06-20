from django.contrib import admin
from .models import Contacts, NeighbourHood, Posts,User,Business

# Register your models here.
admin.site.register(NeighbourHood)
admin.site.register(User)
admin.site.register(Business)
admin.site.register(Contacts)
admin.site.register(Posts)