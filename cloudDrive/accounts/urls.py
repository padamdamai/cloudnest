from django.urls import path
from .views import * 

urlpatterns = [
    path('cloudNest/register',registerUser),
    path('cloudNest/login/',login_user),
    path('cloudNest/logout/',logout_user)
]
