from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class SignUpForm(UserCreationForm):
    First_name=forms.CharField(max_length=30 ,required =False,help_text='Optional')
    last_name=forms.CharField(max_length=30 ,required =False,help_text='Optional')
    email =forms.EmailField(max_length=254,help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
        'username',
        'First_name',
        'last_name',
        'email',
        'password1',
        'password2',
        ]
class Authenticate(AuthenticationForm):
    username = forms.CharField(max_length=30,help_text='Enter a valid username')
    password = forms.CharField(widget=forms.PasswordInput,help_text='Enter a valid password')

    class Meta:
        model = User
