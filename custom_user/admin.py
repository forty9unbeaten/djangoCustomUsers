from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from custom_user.models import MyCustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Misc. Settings', {
            "fields": [
                'homepage',
                'display_name',
                'age'
            ],
        }),
    )


admin.site.register(MyCustomUser, CustomUserAdmin)
