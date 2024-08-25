from django.urls import path
from .views import * 

urlpatterns = [
    path('',home),
    path('cloudNest/Innerfolder/<int:folder_id>',innerFolder, name="folder"), 
    path('cloudNest/subFolder/<int:subfolder_id>', subFile, name='subFile'),
    path('cloudNest/renameFolder/<int:rename_id>', renameFolder, name='renameFolder'),
    path('cloudNest/deleteFolder/<int:delete_id>', deleteFolder, name='deleteFolder'),
    path('cloudNest/dowlnoadFolder/<int:folder_id>', download_folder, name='dowlnoadFolder'),
    path('cloudNest/renameFile/<int:renameFile_id>', renameFile, name='renameFile'),
    path('cloudNest/renameInnerFolder/<int:folder_id>/<int:innerFolderRename_id>', innerFolderRename, name='innerFolderRename'),
    path('cloudNest/deleteInnerFolder/<int:delete_InnerFolderID>',deleteFolder,name='deleteFolder')






]
