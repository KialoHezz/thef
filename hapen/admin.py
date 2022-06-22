from django.contrib import admin
from .models import Contacts, NeighbourHood, Posts,User,Business,Comment


# Register your models here.
admin.site.register(NeighbourHood)
admin.site.register(User)
admin.site.register(Business)
admin.site.register(Posts)
admin.site.register(Comment)
admin.site.register(Contacts)


