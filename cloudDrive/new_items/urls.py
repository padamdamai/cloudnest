from django.urls import path
from .views import * 

urlpatterns = [
    path('CloudNest/NewFolder/',NewFolder)
]