from attr import field
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', "password2"]


# Modification

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'username']


class ProfileUpadateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
