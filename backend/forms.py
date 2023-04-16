from django import forms
from django.contrib.auth.forms import AuthenticationForm

from backend.models import User

class UserLoginForm(AuthenticationForm):
    pass