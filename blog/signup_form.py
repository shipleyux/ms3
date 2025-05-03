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
        Profile = apps.get_model('blog', 'Profile')
        Profile.objects.update_or_create(
            user=user,
            defaults={'display_name': self.cleaned_data['display_name']}
        )
        return user

