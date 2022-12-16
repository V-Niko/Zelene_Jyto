from django.urls import path, include
from .views import *

urlpatterns = [
    path('2003/', special_case_2003),
    path('<int:year>/', year_archive),
    path('<int:year>/<int:month>/', month_archive),
]