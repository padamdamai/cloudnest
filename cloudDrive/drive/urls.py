from django.urls import path
from .views import * 

urlpatterns = [
    path('',home),
    path('cloudNest/folder/<int:folder_id>',innerFolder, name="folder"), 
    path('cloudNest/subFolder/<int:subfolder_id>', subFile, name='subFile'),
    path('cloudNest/renameFolder/<int:rename_id>', renameFolder, name='renameFolder'),
    path('cloudNest/deleteFolder/<int:delete_id>', deleteFolder, name='deleteFolder'),
    path('cloudNest/dowlnoadFolder/<int:folder_id>', download_folder, name='dowlnoadFolder'),
    path('cloudNest/renameFile/<int:renameFile_id>', renameFile, name='renameFile')





]
