from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms.models import ModelForm

from .models import Profile


class RegisterForm(ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2


class ProUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['address','profession','hobby','biography']