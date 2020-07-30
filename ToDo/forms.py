from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('name', 'username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)


class AddForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add To Dos'}))
