from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db.models import Model, CharField, DateTimeField, BooleanField

class CustomUser(AbstractUser):

    username = CharField(
        'Username',
        max_length=150,
        unique=True
    )

    password = CharField(
        'Password',
        max_length=120,
    )

    is_active = BooleanField(default=True)

    create_date = DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.username
