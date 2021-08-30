from django.contrib.admin import register, ModelAdmin

from apps.users.models import CustomUser

@register(CustomUser)
class UserAdmin(ModelAdmin):
    list_display = ('username', 'password', 'create_date', 'is_active')
    ordering = ('username',)
