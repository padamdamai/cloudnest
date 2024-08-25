from django.shortcuts import render,redirect,get_object_or_404,reverse
from .models import *
from django.contrib import messages
from django.http import HttpResponse
import os
import zipfile
import io

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
        'innerFile':innerFile,
        'parentFolderId' : parentfolder
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

def renameFolder(request,rename_id):
    if request.user.is_authenticated:
        folders = Folder.objects.filter(folderUser=request.user).order_by('-id')
        files = File.objects.filter(fileUser=request.user).order_by('-id')
        
        # Get the folder instance to be renamed
        folder_instance = get_object_or_404(Folder, id=rename_id, folderUser=request.user)
        
        if request.method == 'POST':
                folder_name = request.POST.get('renameFolder')
                
                if folder_name:
                    folder_instance.folderName = folder_name
                    folder_instance.save()
                    print('updated folder name')
                    return redirect('/')
    context = {
        'folders':folders,
        'files':files,
        'rename_id': rename_id
    }
    return render(request,'rename.html',context)

def deleteFolder(request, delete_id):
    if request.user.is_authenticated:
        folder_instance = get_object_or_404(Folder, id=delete_id, folderUser=request.user)
        folder_instance.delete()
        print('folder deleted')
        return redirect('/')
    else:
        print('else part ')


def download_folder(request, folder_id):
    if request.user.is_authenticated:
        # Fetch the folder instance and ensure it belongs to the authenticated user
        folder_instance = get_object_or_404(Folder, id=folder_id, folderUser=request.user)

        # Path where the folder's contents are located
        base_path = '/path/to/your/folders'
        folder_path = os.path.join(base_path, folder_instance.folderName)

        # Create a BytesIO buffer to hold the ZIP file content
        buffer = io.BytesIO()

        # Create a ZIP file in the buffer
        with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            # Walk through the directory and add files to the ZIP file
            for root, dirs, files in os.walk(folder_path):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    # Calculate the relative path for the file within the ZIP
                    # Relative to the base folder
                    arcname = os.path.relpath(file_path, base_path)
                    zip_file.write(file_path, arcname=arcname)

        # Set the buffer's position to the beginning
        buffer.seek(0)

        # Create an HTTP response with the ZIP file
        response = HttpResponse(buffer, content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename="{folder_instance.folderName}.zip"'
        
        return response
    else:
        return redirect('login')  # Redirect to login if the user is not authenticated


def renameFile(request,renameFile_id):
    if request.user.is_authenticated:
        folders = Folder.objects.filter(folderUser=request.user).order_by('-id')
        files = File.objects.filter(fileUser=request.user).order_by('-id')
        
        # Get the folder instance to be renamed
        file_instance = get_object_or_404(File, id=renameFile_id, fileUser=request.user)
        
        if request.method == 'POST':
            file_name = request.POST.get('renameFile')
            
            if file_name:
                file_instance.file = file_name
                file_instance.save()
                print('updated folder name')
                return redirect('/')
    context = {
        'folders':folders,
        'files':files,
        'rename_id': renameFile_id
    }
    return render(request,'renameFIle.html',context)


def innerFolderRename(request,folder_id ,innerFolderRename_id):
    parentfolder = Folder.objects.get(id=folder_id)
    innerFolder = InnerFolder.objects.filter(parentFolder=folder_id).order_by('-id')
    innerFile = InnerFile.objects.filter(fileUser = parentfolder)

    folder_instance = get_object_or_404(InnerFolder, id=innerFolderRename_id)
    if request.method == 'POST':
            folder_name = request.POST.get('renameFolder')
            
            if folder_name:
                    folder_instance.folderName = folder_name
                    folder_instance.save()
                    print('updated folder name')
                    return redirect('folder', folder_id=folder_id)
    context = {
        'innerFolder':innerFolder,
        'folderId':folder_id,
        'innerFile':innerFile,
        'renaming_folder_id': innerFolderRename_id 
    }

    return render(request,'innerFolderRename.html',context) 

def deleteFolder(request,delete_InnerFolderID):
    if request.user.is_authenticated:
        folder_instance = get_object_or_404(InnerFolder, id=delete_InnerFolderID)
        folder_instance.delete()
        print('folder deleted')
        return redirect('folder',folder_id =delete_InnerFolderID)
    else:
        print('else part ')