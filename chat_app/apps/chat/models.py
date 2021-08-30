from django.db.models import Model, TextField, DateTimeField, ForeignKey, CASCADE, CharField

from apps.users.models import CustomUser

class Room(Model):
    owner = ForeignKey(CustomUser, on_delete=CASCADE)
    name = CharField(unique=True, max_length=50)
    create_date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Message(Model):
    content = TextField()
    timestamp = DateTimeField(auto_now_add=True)
    room = ForeignKey(Room, on_delete=CASCADE)
    owner = CharField(max_length=150)

    def __str__(self):
        return self.content

