from django.urls import path, include
from .views import *

urlpatterns = [
    path('add/', add),
    path('delete/', delete),
    path('edit/', edit)
]