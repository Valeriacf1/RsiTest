from django.urls import path
from . import views
from .views import list_employee, add_employee
urlpatterns = [
    path('list/', list_employee, name="list_employee"),
     path('addEmployee/', add_employee, name="add_employee"),
]


