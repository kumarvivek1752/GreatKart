from dataclasses import field
from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class AccountAdmin(UserAdmin):
    list_display=('email','first_name','last_name','last_login','date_joined','is_active') # display items in user row
    list_display_links=('email','first_name','last_name')# for links clickable in user row
    readonly_fields = ('last_login','date_joined')# for readonly fields
    ordering=('-date_joined',)#for formatting date

    #important when we are using costom user model
    filter_horizontal=()
    list_filter=()
    fieldsets=() # for password noneditable



admin.site.register(Account,AccountAdmin)