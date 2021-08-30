from django.core.exceptions import ValidationError
from django.forms import CharField, PasswordInput, Form
from django.contrib.auth.forms import UserCreationForm

from apps.users.models import CustomUser

class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        exclude = [
            'last_login', 'date_joined', 'password'
        ]

class LogInForm(Form):

    username = CharField(required=True, max_length=150)
    password = CharField(required=True, max_length=120)

    def clean(self):
        clean_data = super().clean()
        user = None
        if clean_data.get('username'):
            user = CustomUser.objects.filter(username=clean_data.get('username'))
            if len(user) == 0 or not user[0].check_password(clean_data.get('password')):
                raise ValidationError('The username or password are wrong')
        return clean_data
