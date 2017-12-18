from django import forms
from django.contrib.auth.models import User

from .models import *

class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = [
            'organization',
            'channel',
            'thematic',
        ]
