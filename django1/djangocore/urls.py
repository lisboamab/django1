from django.urls import path
# from django.contrib import admin
from .views import index, contato

urlpatterns = [
    path('', 'index.html'),
    path('contato', 'contato.html'),
    
]
