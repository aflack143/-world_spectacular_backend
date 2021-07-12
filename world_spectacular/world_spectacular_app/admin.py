from django.contrib import admin
from .models import Country, Country_Picture, User, User_Visit

admin.site.register(Country)
admin.site.register(Country_Picture)
admin.site.register(User)
admin.site.register(User_Visit)