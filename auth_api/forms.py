from django.contrib.auth.forms import AuthenticationForm
from .models import Profile


class LoginForm(AuthenticationForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'second_name', 'password', 'role')
