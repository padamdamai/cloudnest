from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        folders = Folder.objects.filter(folderUser=request.user).order_by('-id')
        files = File.objects.filter(fileUser=request.user).order_by('-id')
        # for uploading folder
        if request.method == 'POST':
            if 'createfolder' in request.POST:
                    foldername = request.POST.get('folder_name')
                    if Folder.objects.filter(folderName = foldername).exists():
                        messages.error(request," folder name already exists")
                        return redirect('/')
                    else:
                        folder = Folder.objects.create(folderName = foldername,folderUser = request.user)
                        if folder:
                            return redirect('/')
                        else:
                            messages.error(request," folder hasn't been created please try again")
                            return redirect('/')
    # for uploading files
            else:
                uploaded = request.FILES.get('uploadFile')
                File.objects.create(file =uploaded,fileUser = request.user)

        context = {
        'folders' : folders,
        'files':files
                }
        return render(request,"home.html",context)
    else:
        return render(request,'home.html')  
      

def innerFolder(request,folder_id):
    parentfolder = Folder.objects.get(id=folder_id)
    innerFolder = InnerFolder.objects.filter(parentFolder=folder_id).order_by('-id')
    if request.method == 'POST':
        if 'folder_name' in request.POST:
            folder_name = request.POST.get('folder_name')
            InnerFolder.objects.create(folderName=folder_name, parentFolder=parentfolder)
        elif 'uploadFile' in request.FILES:
            print("File upload block reached.")
            uploaded_file = request.FILES['uploadFile']
            print(f"File uploaded: {uploaded_file.name}")
            InnerFile.objects.create(file=uploaded_file, fileUser=parentfolder)
        else:
            print("No recognized POST fields.")



    context = {
        'innerFolder':innerFolder,
        'folderId':folder_id,
    }

    return render(request,'innerFolder.html',context)   

def subFolder(request,subfolder_id):
    folder_User = InnerFolder.objects.get(id = subfolder_id,)
    innerFolder = SubFolder.objects.filter(parentFolder=folder_User).order_by('-id')
    if request.method == 'POST':
        folder_name = request.POST['folder_name']
        SubFolder.objects.create(folderName = folder_name ,parentFolder =folder_User)

    context = {
        'subfolder':innerFolder,
        'subfolderId':subfolder_id
    }

    return render(request,'subfolder.html',context)   