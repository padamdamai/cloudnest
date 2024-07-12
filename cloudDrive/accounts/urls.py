from django.urls import path
from .views import * 

urlpatterns = [
    path('',registerUser),
    path('login/',login_user)
]
