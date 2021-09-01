from django.forms import ModelForm

from apps.chat.models import Room

class RoomForm(ModelForm):

    class Meta:
        model = Room
        exclude = [
            'owner', 'create_date'
        ]
