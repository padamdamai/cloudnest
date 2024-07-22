from django.shortcuts import render,redirect
from .models import * 
from django.contrib import messages
# Create your views here.
def NewFolder(request):
    if request.method == 'POST':
        folder_name = request.POST['folder_name']
        folder = Folder.objects.create(folderName = folder_name)
        if folder:
            messages.success(request,'folder created successfully')
            return redirect('/')
        else:
            messages.error(request," folder hasn't been created please try again")
            return redirect('/')
    return render(request,'home.html')
