from django.contrib.auth.models import User
from django.db import models

# Create your models here.

from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserCreateForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None