from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin, admin.ModelAdmin):
    fieldsets = (
        ('User info', {'fields': (
        'username', 'password', 'first_name', 'last_name', 'email', 'status', 'about_yourself')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser',
            'status', 'about_yourself'),
        }),
    )