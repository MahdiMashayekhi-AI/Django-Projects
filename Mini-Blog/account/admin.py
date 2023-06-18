from django.contrib import admin
from . import models

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'display_image',
        'username',
        'get_full_name',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'is_superuser',
        'date_joined',
    ]
    list_filter = [
        'is_active',
        'is_staff',
    ]
    search_fields = [
        'username',
        'email',
    ]
    list_editable = [
        'is_staff',
        'is_active',
        'is_superuser',
    ]
    list_display_links = [
        'username',
        'first_name',
        'last_name',
    ]
    ordering = [
        '-date_joined',
        'username',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        ]
    list_per_page = 50


admin.site.register(models.Account, AccountAdmin)
