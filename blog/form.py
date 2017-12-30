from django import forms
from .models import BlogUser

from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True

    class Meta:
        model = BlogUser
        fields = ("username", 'email', 'full_name', 'address', 'phone_number', 'type')
