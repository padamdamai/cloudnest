from django.forms import ModelForm
from .models import *

class CreateFolder(ModelForm):
    class Meta:
        model = Folder
        fields = "__all__"

class CreateFile(ModelForm):
    class Meta:
        model = File
        fields = "__all__"