from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserVerification

class AccountUserAdmin(UserAdmin):
    list_display = ('id','email', 'first_name', 'last_name', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['email']
    fieldsets = [
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'profile_pic')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    ]
 
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_active', 'is_staff')}
        ),
    )

admin.site.register(User, AccountUserAdmin)
admin.site.register(UserVerification)