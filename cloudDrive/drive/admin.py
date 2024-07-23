from django.contrib import admin
from .models import * 
# Register your models here.
@admin.register(Folder)
class Adminfolder(admin.ModelAdmin):
    list_display=('folderName','folderUser')