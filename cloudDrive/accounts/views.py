from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import * 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def registerUser(request):
    if request.method == 'POST':
        register_user = UserCreationForm(request.POST)
        if register_user.is_valid():
            register_user.save()
            messages.add_message(request,messages.SUCCESS,'You are successfully registered')
            return redirect('/login/')
        else:
            messages.add_message(request,messages.ERROR,'something went wrong please try again!!')
            return render(request,'register.html')

    context ={
        "Registration_form": UserCreationForm
    }
    return render(request,'register.html',context)

def login_user(request):
    if request.method == 'POST':
        Login = Login_user(request.POST)
        if Login.is_valid():
            data = Login.cleaned_data
            user = authenticate(request,username=data['username'],password = data['password'])
        if user is not None:
            login(request,user)      
            messages.add_message(request,messages.SUCCESS,'successfully login')
            return redirect('/home')
        else:
            messages.add_message(request,messages.ERROR,'Something went wrong')
            return redirect('/login')


        
    context = {
        'Login_user':Login_user()
    }
    return render(request,'login.html',context)