from django.contrib.auth.forms import AuthenticationForm, BaseUserCreationForm, UserCreationForm
from .models import Profile


class LoginForm(AuthenticationForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'second_name', 'password', 'role')


class RegisterForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'second_name')


    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.password = self.cleaned_data['password']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
