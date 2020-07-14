from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


class CustomUserAdmin(UserAdmin):
    """Add new fields to the admin"""
    fieldsets = ((None, {'fields': ('username', 'password')}),
                 ('Personal info', {'fields': ('first_name', 'middle_name', 'last_name', 'email')}),
                 ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
                 ('Important dates', {'fields': ('last_login', 'date_joined')}))


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
