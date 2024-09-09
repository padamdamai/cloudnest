from django.shortcuts import render,redirect
from .forms import * 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def registerUser(request):
    if request.method == 'POST':
        register_user = CustomUserCreationForm(request.POST)
        if register_user.is_valid():
            register_user.save()
            messages.add_message(request,messages.SUCCESS,'You are successfully registered')
            return redirect('/cloudNest/login/')
        else:
            for field, errors in register_user.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")

    return render(request,'register.html',{'Registration_form':CustomUserCreationForm})


def login_user(request):
            if request.method == 'POST':
                Login = Login_user(request.POST)
                if Login.is_valid():
                    data = Login.cleaned_data
                    user = authenticate(request,username=data['username'],password = data['password'])
                if user is not None:
                    login(request,user)      
                    messages.add_message(request,messages.SUCCESS,'successfully login')
                    return redirect('/')
                else:
                    messages.add_message(request,messages.ERROR,"Your credentials do not match our records.")
                    return redirect('/cloudNest/login/')


                
            context = {
                'Login_user':Login_user()
            }
            return render(request,'login.html',context)

@login_required
def logout_user(request):
    logout(request)
    print(" logout function called ")
    return redirect('/')