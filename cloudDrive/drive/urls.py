from django.urls import path,include
from .views import * 

urlpatterns = [
    path('',home),
    path('cloudNest/files/<int:folder_id>',files,name="folder")    
]
