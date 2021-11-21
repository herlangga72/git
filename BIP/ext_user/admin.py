from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# future refactor = for performance wise maybe just insert it to user Admin field sets??

# copy value fieldset then insert the extended one. next replace it

fields = list(UserAdmin.fieldsets)

fields.insert( 2, ( 'Extended Info', { 'fields': ('is_pekerti_peserta','avatar') } ) )

UserAdmin.fieldsets = tuple(fields)

admin.site.register (User, UserAdmin)