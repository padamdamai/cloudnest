from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=150,
                                       widget=forms.TextInput(attrs={
            'class': 'form-control my-custom-class',  # Custom CSS class
            'placeholder': 'Enter your username',    # Placeholder text
        }))  
    
    email = forms.EmailField(label='email', widget=forms.TextInput(attrs={
            'class': 'form-control my-custom-class',  # Custom CSS class
            'placeholder': 'Enter your email',    # Placeholder text
        })) 
     
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={
            'class': 'form-control my-custom-class',  # Custom CSS class
            'placeholder': 'Enter your password',    # Placeholder text
        }))   
    
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={
            'class': 'form-control my-custom-class',  # Custom CSS class
            'placeholder': 'retype your password',    # Placeholder text
        }))   
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Field('username', css_class='form-control my-custom-class'),
            Field('email', css_class='form-control my-custom-class'),
            Field('password1', css_class='form-control my-custom-class'),
            Field('password2', css_class='form-control my-custom-class')

        )
        self.helper.add_input(Submit('submit', 'Register', css_class='p-2 w-100 rounded'))


    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username=username)  
        if new.exists():  
            raise forms.ValidationError("User already exists.")  
        return username
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.exists():  
            raise forms.ValidationError("Email already exists.")  
        return email
    
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise forms.ValidationError("Passwords don't match.")  
        return password2
    
    def save(self, commit=True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']
        )  
        return user


class Login_user(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control my-custom-class',  # Custom CSS class
            'placeholder': 'Enter your username',    # Placeholder text
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control my-custom-class',
            'placeholder': 'Enter your password',
        })
    )

    def __init__(self, *args, **kwargs):
        super(Login_user, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Field('username', css_class='form-control my-custom-class'),
            Field('password', css_class='form-control my-custom-class'),
        )
        self.helper.add_input(Submit('submit', 'Login', css_class='p-2 w-100 bg_success_loggedIn rounded'))