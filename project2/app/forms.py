from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {'password':forms.PasswordInput}
        help_texts = {'username':'', 'password':'Please enter the valid password'}

