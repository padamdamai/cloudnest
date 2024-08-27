from django.shortcuts import render,redirect,get_object_or_404,reverse
from .models import *
from django.contrib import messages
from django.http import HttpResponse,FileResponse,Http404
import os

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

def subFile(request,innerFolderId):
    folder_User = InnerFolder.objects.get(id = innerFolderId,)
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
        'innerfolderId':innerFolderId
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

def deleteFile(request,file_Id):
    if request.user.is_authenticated:
        file_instance = get_object_or_404(File, id=file_Id)
        file_instance.delete()
        print('folder deleted')
        return redirect('/')
    else:
        print('else part ')

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

def deleteInnerFolder(request,parentfolder_id,delete_InnerFolderID):
    if request.user.is_authenticated:
        folder_instance = get_object_or_404(InnerFolder, id=delete_InnerFolderID)
        folder_instance.delete()
        print('folder deleted')
        return redirect('folder',folder_id = parentfolder_id)
    else:
        print('else part ')
    
def renameInnerFile(request,parentFOlderiD,renamefile_Id):
    parentfolder = Folder.objects.get(id=parentFOlderiD)
    innerFolder = InnerFolder.objects.filter(parentFolder=parentFOlderiD).order_by('-id')
    innerFile = InnerFile.objects.filter(fileUser = parentfolder)

    folder_instance = get_object_or_404(InnerFile, id=renamefile_Id)
    if request.method == 'POST':
            file_name = request.POST.get('renameFile')
            if file_name:
                    folder_instance.file = file_name
                    folder_instance.save()
                    print('updated folder name')
                    return redirect('folder', folder_id=parentFOlderiD)
    context = {
        'innerFolder':innerFolder,
        'folderId':parentFOlderiD,
        'innerFile':innerFile,
        'renaming_file_id': renamefile_Id 
    }

    return render(request,'renameInnerFile.html',context) 

def  deleteInnerFile(request,parentFolder_id,deleteInnerfile_Id):
    if request.user.is_authenticated:
        folder_instance = get_object_or_404(InnerFile, id = deleteInnerfile_Id)
        folder_instance.delete()
        print('folder deleted')
        return redirect('folder',folder_id = parentFolder_id)
    else:
        print('else part ')

def downloadInnerFile(request,fileDownloadInner_id):
    file_instance = get_object_or_404(InnerFile, id=fileDownloadInner_id)
    file_path = file_instance.file.path 

    try:
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{file_instance.file.name}"'
        return response
    except FileNotFoundError:
        raise Http404("File does not exist")
    
def downloadFile(request,fileDownload_id):
    try:
        file_instance = get_object_or_404(File, id=fileDownload_id)
        file_path = file_instance.file.path 
        print(f"File Path: {file_path}")

        # Check if the file exists
        if not os.path.exists(file_path):
            print("File does not exist")
            raise Http404("File does not exist")

        # Serving the file
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{file_instance.file.name}"'
        print("File is being downloaded")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise Http404("File does not exist")
    
def renameSubFile(request,innerfolderId,renameSubFile_id):
    folder_User = InnerFolder.objects.get(id = innerfolderId,)
    subFile = SubFile.objects.filter(fileUser=folder_User).order_by('-id')
    file_instance = get_object_or_404(SubFile, id=renameSubFile_id)
        
    if request.method == 'POST':
        file_name = request.POST.get('renameSubFile')
            
        if file_name:
            file_instance.file = file_name
            file_instance.save()
            return redirect('subFile', innerFolderId = innerfolderId)

    context = { 
        'subfile':subFile,  
        'innerfolderId':innerfolderId,
        'renameSubFile_id':renameSubFile_id
    }

    return render(request,'subfileRename.html',context)  

def deleteSubFile(request,innerfolderId,deleteSubFile_id):
    if request.user.is_authenticated:
        file_instance = get_object_or_404(SubFile,id= deleteSubFile_id)
        file_instance.delete()
        return redirect('subFile', innerFolderId = innerfolderId)
    
    
def downloadSubFile(request, downloadSubFile_id):
    try:
        file_instance = get_object_or_404(SubFile, id=downloadSubFile_id)
        file_path = file_instance.file.path 
        print(f"File Path: {file_path}")
        if not os.path.exists(file_path):
            print("File does not exist")
            raise Http404("File does not exist")

        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{file_instance.file.name}"'
        print("File is being downloaded")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise Http404("File does not exist")