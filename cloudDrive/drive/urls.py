from django.urls import path
from .views import * 

urlpatterns = [
    path('',home),
    path('cloudNest/Innerfolder/<int:folder_id>',innerFolder, name="folder"), 
    path('cloudNest/subFolder/<int:innerFolderId>', subFile, name='subFile'),
    path('cloudNest/renameFolder/<int:rename_id>', renameFolder, name='renameFolder'),
    path('cloudNest/<int:delete_id>', deleteFolder, name='deleteFolder'),
    path('cloudNest/renameFile/<int:renameFile_id>', renameFile, name='renameFile'),
    path('cloudNest/renameInnerFolder/<int:folder_id>/<int:innerFolderRename_id>', innerFolderRename, name='innerFolderRename'),
    path('cloudNest/<int:parentfolder_id>/<int:delete_InnerFolderID>',deleteInnerFolder,name='deleteInnerFolder'),
    path('cloudNest/renameInnerFile/<int:parentFOlderiD>/<int:renamefile_Id>/',renameInnerFile,name='renameInnerFile'),
    path('cloudNest/<int:file_Id>/',deleteFile,name='deleteFile'),
    path('cloudNest/<int:parentFolder_id>/<int:deleteInnerfile_Id>/',deleteInnerFile,name='deleteInnerFile'),
    path('cloudNest/<int:fileDownloadInner_id>/', downloadInnerFile, name='downloadInnerFile'),
    path('CloudNest/<int:fileDownload_id>/', downloadFile, name='downloadFile'),
    path('CloudNest/renameSubFIle/<int:innerfolderId>/<int:renameSubFile_id>/', renameSubFile, name='renameSubFile'),
    path('CloudNest/<int:innerfolderId>/<int:deleteSubFile_id>/', deleteSubFile, name='deleteSubFile'),
    path('CloudNest/<int:downloadSubFile_id>', downloadSubFile, name='downloadSubFile'),
    path('CloudNest/search',searchFiles,name='search'),

    path('CloudNest/<str:model_name>/rename/<int:id>/' ,SearchrenameFile , name="SearchrenameFile"),
    path('CloudNest/<str:model_name>/rename/<int:id>/' ,SearchrenameFile , name="SearchdeleteFile"),
    path('CloudNest/<str:model_name>/rename/<int:id>/' ,SearchrenameFile , name="SearchdownloadFile")




]
