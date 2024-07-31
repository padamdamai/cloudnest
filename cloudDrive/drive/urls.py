from django.urls import path
from .views import * 

urlpatterns = [
    path('',home),
    path('cloudNest/folder/<int:folder_id>',innerFolder, name="folder"), 
    path('cloudNest/subFolder/<int:subfolder_id>', subFile, name='subFile'),
    path('cloudNest/testuploadfolder/', testuploadfolder, name='testuploadfolder'),

]
