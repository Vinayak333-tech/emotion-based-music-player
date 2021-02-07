from django import forms
from .models import *


class SongUploadForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['track','name']
