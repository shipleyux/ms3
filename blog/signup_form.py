# blog/signup_form.py

from django import forms
from allauth.account.forms import SignupForm
from django.apps import apps


class CustomSignupForm(SignupForm):
    display_name = forms.CharField(
        max_length=100,
        label='Display Name',
        required=True
    )

    def save(self, request):
        user = super().save(request)
       
       
        return user

