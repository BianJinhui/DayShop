from django.urls import path
from Seller.views import *
urlpatterns = [
    path('login/', login),
    path('register/', register),
    path('register_store/', register_store),
]