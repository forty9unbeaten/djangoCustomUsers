from django import forms
from custom_user.models import MyCustomUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.ModelForm):
    class Meta:
        model = MyCustomUser
        fields = [
            'display_name',
            'homepage',
            'age'
        ]
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
