from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Folder(models.Model):
    folderName= models.CharField(max_length=50,default='Folder',null=True)
    folderUser = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.folderName

class InnerFolder(models.Model):
    folderName= models.CharField(max_length=50,default='Folder')
    folderUser = models.ForeignKey(Folder,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.folderName

class File(models.Model):
    file = models.FileField(upload_to='files',null=False)
    fileUser = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
