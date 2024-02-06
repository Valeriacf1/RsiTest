from django.urls import path
from . import views
from .views import departmentlist, add_department, remove_department



urlpatterns = [
    path('department/', views.departmentlist, name="list_department"),
    path('departmentlist/', departmentlist, name='departmentlist'),
    path('add_department/', views.add_department, name='add_department'),
    path('remove_department/<int:department_id>/', remove_department, name='remove_department'),
]


