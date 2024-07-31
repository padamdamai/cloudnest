from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
MAX_FILENAME_LENGTH = 15 
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
            elif 'uploadFolder' in request.POST:
                uploadFolder = request.FILES.get('uploadFOLDER')
                Folder.objects.create(folderName = uploadFolder,folderUser = request.user)
                
    # for uploading files
            else:
                uploaded = request.FILES.get('uploadFile')
                file_name = uploaded.name
                if len(file_name) > MAX_FILENAME_LENGTH:
                    messages.error(request,"Rename your file name ,length of the file name should be less than 11 character  ")
                else:
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
    innerFile = InnerFile.objects.filter(fileUser = parentfolder)
    if request.method == 'POST':
        if 'folder_name' in request.POST:
            folder_name = request.POST.get('folder_name')
            InnerFolder.objects.create(folderName=folder_name, parentFolder=parentfolder)
        elif 'uploadFile' in request.FILES:
            uploaded_file = request.FILES['uploadFile']
            file_name = uploaded_file.name
            if len(file_name) > MAX_FILENAME_LENGTH :
                messages.error(request,"Rename your file name ,length of the file name should be less than 11 character  ")
            else:
                InnerFile.objects.create(file=uploaded_file, fileUser=parentfolder)
        else:
            print("No recognized POST fields.")

    

    context = {
        'innerFolder':innerFolder,
        'folderId':folder_id,
        'innerFile':innerFile
    }

    return render(request,'innerFolder.html',context)   

def subFile(request,subfolder_id):
    folder_User = InnerFolder.objects.get(id = subfolder_id,)
    subFile = SubFile.objects.filter(fileUser=folder_User).order_by('-id')
    if request.method == 'POST':
            uploaded_file = request.FILES['uploadFile']
            file_name = uploaded_file.name
            if len(file_name) > MAX_FILENAME_LENGTH :
                messages.error(request,"Rename your file name ,length of the file name should be less than 11 character  ")
            else:
                SubFile.objects.create(file=uploaded_file, fileUser=folder_User)

    context = {
        'subfile':subFile,  
        'innerfolderId':subfolder_id
    }

    return render(request,'subfolder.html',context)   


def testuploadfolder(request):
    if request.method == 'POST':
        print(f'hello uploaded folder')