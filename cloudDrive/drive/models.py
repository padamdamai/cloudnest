from django.db import models

# Create your models here.
class Folder(models.Model):
    name= models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

    def __self__(self):
        return self.name