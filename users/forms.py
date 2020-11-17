from django.contrib.auth.forms import UserCreationForm as create_account
from django import forms
from .models import User

class UserCreationForm(create_account):
    class Meta(create_account.Meta):
        model = User
        fields = create_account.Meta.fields
