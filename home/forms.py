from django.shortcuts import redirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from . models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        field = ('first_name', 'last_name', 'email')

    class ProfileForm(forms.ModelForm):
        class Meta:
            model = Profile
            field = ('bio', 'birth_date')