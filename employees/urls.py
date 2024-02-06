from django.urls import path
from . import views
from .views import list_employee, add_employee, remove_employee
urlpatterns = [
    path('list/', views.list_employee, name="list_employee"),
    path('addEmployee/', views.add_employee, name="add_employee"),
    path('remove_employee/<int:employee_id>/', views.remove_employee, name='remove_employee'),
]


