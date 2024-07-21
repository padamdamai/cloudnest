from django.db import models

# Create your models here.
class Folder(models.Model):
    folderName= models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.folderName