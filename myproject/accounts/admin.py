from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Customize the display of fields in the admin list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')

    # Fields to search for in the admin interface
    search_fields = ('username', 'email')

    # Fields to filter by in the admin interface
    list_filter = ('is_staff', 'is_active', 'is_superuser')
