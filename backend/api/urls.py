from django.urls import path
from .views import register,register_page

urlpatterns = [
    path('register/',register),
    path('register_page/',register_page),
]