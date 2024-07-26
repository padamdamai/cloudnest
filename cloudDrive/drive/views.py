from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        folders = Folder.objects.filter(folderUser=request.user).order_by('-id')
        if request.method == 'POST':
            folder_name = request.POST['folder_name']
            if Folder.objects.filter(folderName = folder_name).exists():
                messages.error(request," folder name already exists")
                return redirect('/')
            else:
                folder = Folder.objects.create(folderName = folder_name,folderUser = request.user)
                if folder:
                    return redirect('/')
                else:
                    messages.error(request," folder hasn't been created please try again")
                    return redirect('/')
        context = {
        'folders' : folders
                }
        return render(request,"home.html",context)
    else:
        return render(request,'home.html')  
      

def innerFolder(request,folder_id):
    folder_User = Folder.objects.get(id=folder_id)
    innerFolder = InnerFolder.objects.filter(folderUser=folder_User).order_by('-id')
    if request.method == 'POST':
        folder_name = request.POST['folder_name']
        folder= InnerFolder.objects.create(folderName = folder_name ,folderUser = folder_User)

    context = {
        'innerFolder':innerFolder,
        'folderId':folder_id
    }

    return render(request,'innerFolder.html',context)   

def uploadFiles(request):
    uploadedFiles = File.objects.get(fileUser = request.user).order_by('-id')
    if request.method == 'POST':
        # print("posted data----------------------------------------------")
        uploaded = request.POST.get['uploadFile']
        File.objects.create(file =uploaded,folderUser = request.user)
    context = {
        'uploadedFiles':uploadedFiles
    }
    return render(request,'home.html',context)