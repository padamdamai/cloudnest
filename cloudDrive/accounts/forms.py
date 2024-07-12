from django import forms

class Login_user(forms.Form):
    username = forms.CharField()
    email=forms.EmailField()
    password= forms.CharField(widget=forms.PasswordInput)