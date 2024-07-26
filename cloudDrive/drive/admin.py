from django.contrib import admin
from .models import * 
# Register your models here.
@admin.register(Folder)
class Adminfolder(admin.ModelAdmin):
    list_display=('folderName','folderUser')

@admin.register(InnerFolder)
class AdminInnerFolder(admin.ModelAdmin):
    list_display=('id','folderName','folderUser')

@admin.register(File)
class AdminInnerFolder(admin.ModelAdmin):
    list_display=('file','folderUser')