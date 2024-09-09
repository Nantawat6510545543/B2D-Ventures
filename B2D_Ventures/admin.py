from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .forms import CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Extras', {
                'fields': (
                    'bio',
                )
            }
        )
    )


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
