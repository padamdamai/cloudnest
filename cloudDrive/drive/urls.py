from django.urls import path
from .views import * 

urlpatterns = [
    path('',home),
    path('cloudNest/Innerfolder/<int:folder_id>',innerFolder, name="folder"), 
    path('cloudNest/subFolder/<int:innerFolderId>', subFile, name='subFile'),
    path('cloudNest/renameFolder/<int:rename_id>', renameFolder, name='renameFolder'),
    path('cloudNest/deleteFolder/<int:delete_id>', deleteFolder, name='deleteFolder'),
    path('cloudNest/renameFile/<int:renameFile_id>', renameFile, name='renameFile'),
    path('cloudNest/renameInnerFolder/<int:folder_id>/<int:innerFolderRename_id>', innerFolderRename, name='innerFolderRename'),
    path('cloudNest/deleteInnerFolder/<int:parentfolder_id>/<int:delete_InnerFolderID>',deleteInnerFolder,name='deleteInnerFolder'),
    path('cloudNest/renameInnerFile/<int:parentFOlderiD>/<int:renamefile_Id>/',renameInnerFile,name='renameInnerFile'),
    path('cloudNest/deleteFile/<int:file_Id>/',deleteFile,name='deleteFile'),
    path('cloudNest/deleteInnerFile/<int:parentFOlderiD>/<int:deleteInnerfile_Id>/',deleteInnerFile,name='deleteInnerFile')









]
