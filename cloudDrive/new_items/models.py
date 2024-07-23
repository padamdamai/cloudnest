from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Folder(models.Model):
    folderName= models.CharField(max_length=50)
    folderUser = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.folderName