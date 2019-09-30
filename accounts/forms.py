from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .choices import CHOICES

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    userType = forms.ChoiceField(choices=CHOICES, label="Profession", initial='', widget=forms.Select(), required=True)


    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'userType', 'password1', 'password2']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['email']