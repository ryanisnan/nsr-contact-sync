from django.contrib import admin
from .models import Contact
from .models import PhoneNumber

admin.site.register(Contact)
admin.site.register(PhoneNumber)