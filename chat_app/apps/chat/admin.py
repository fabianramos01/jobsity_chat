from django.contrib.admin import ModelAdmin, register

from apps.chat.models import Message, Room

@register(Message)
class RoleAdmin(ModelAdmin):
    list_display = ('content', 'room', 'owner', 'timestamp')
    ordering = ('-timestamp',)

@register(Room)
class RoomAdmin(ModelAdmin):
    list_display = ('name', 'owner', 'create_date')
    ordering = ('-create_date',)
