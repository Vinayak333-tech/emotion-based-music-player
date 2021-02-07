from django import forms
from .models import *


class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = ['image']
