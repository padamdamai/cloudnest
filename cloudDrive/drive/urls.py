from django.urls import path,include
from .views import * 

urlpatterns = [
    path('',home),
    path('cloudNest/files/<int:folder_id>',innerFolder, name="folder"), 
    path('cloudNest/upload_files',uploadFiles,name= 'upload_files')   
]
