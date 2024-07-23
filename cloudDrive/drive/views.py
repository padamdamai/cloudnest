from django.shortcuts import render,redirect
from new_items.models import *
from django.contrib import messages
# from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    folders = Folder.objects.filter(folderName=request.user).order_by('-id')
    if request.method == 'POST':
        folder_name = request.POST['folder_name']
        if Folder.objects.filter(folderName = folder_name).exists():
            messages.error(request," folder name already exists")
            return redirect('/')
        else:
            folder = Folder.objects.create(folderName = folder_name,folderUser = request.user)
            if folder:
                messages.success(request,'folder created successfully')
                return redirect('/')
            else:
                messages.error(request," folder hasn't been created please try again")
                return redirect('/')
      
          
    context = {
        'folders' : folders
                }
    return render(request,"home.html",context)