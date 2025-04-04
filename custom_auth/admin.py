from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

class UserAbsAdmin(UserAdmin):
    list_display = ('username', 'email', 'telefone', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('telefone')})
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('telefone')})
    )
admin.site.register(CustomUser)