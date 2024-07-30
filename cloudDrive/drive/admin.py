from django.contrib import admin
from .models import * 
# Register your models here.
@admin.register(Folder)
class Adminfolder(admin.ModelAdmin):
    list_display=('folderName','folderUser')

@admin.register(InnerFolder)
class AdminInnerFolder(admin.ModelAdmin):
    list_display=('id','folderName','parentFolder')

@admin.register(File)
class AdminInnerFile(admin.ModelAdmin):
    list_display=('file','fileUser')

@admin.register(SubFolder)
class AdminSubFolder(admin.ModelAdmin):
    list_display=('folderName','parentFolder')

@admin.register(InnerFile)
class AdminInnerFile(admin.ModelAdmin):
    list_display=('file','fileUser')