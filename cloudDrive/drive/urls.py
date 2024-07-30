from django.urls import path,include
from .views import * 

urlpatterns = [
    path('',home),
    path('cloudNest/folder/<int:folder_id>',innerFolder, name="folder"), 
    path('cloudNest/subFolder/<int:subfolder_id>', subFolder, name='subFolder'),

]
