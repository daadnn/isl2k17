from django import forms
from django.contrib.auth.models import User

from .models import *

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = [
            'organization',
            'owner',
        ]
