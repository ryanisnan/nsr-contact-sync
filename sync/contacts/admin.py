from django.contrib import admin
from .models import Contact
from .models import PhoneNumber

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company', 'title')
    list_filter = ('company',)


class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('contact', 'name', 'name_if_other', 'value')

admin.site.register(Contact, ContactAdmin)
admin.site.register(PhoneNumber, PhoneNumberAdmin)