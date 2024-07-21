from django.shortcuts import render,redirect
from new_items.models import *

# Create your views here.
def home(request):
    folders = Folder.objects.all().order_by('-id')
    # print(folders)
    context = {
        'folders' : folders
                }
    return render(request,"home.html",context)