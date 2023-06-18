from django.contrib import admin
from django.utils.html import format_html
from django.templatetags.static import static
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

    @staticmethod
    def display_image(obj):
        if obj.image:
            return format_html('<img src="{}" width="35" height="35" />', obj.image.url)
        else:
            default_avatar = static('src/images/avatars/avatar_default.png')
            return format_html('<img src="{}" width="35" height="35" />', default_avatar)


    display_image.short_description = 'Image'

admin.site.register(models.Account, AccountAdmin)
