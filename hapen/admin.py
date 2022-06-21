from django.contrib import admin
from .models import NeighbourHood,User,Business,Posts,Comment

# Register your models here.
admin.site.register(NeighbourHood)
admin.site.register(User)
admin.site.register(Business)
admin.site.register(Posts)
admin.site.register(Comment)