from django.urls import path
from .views import departmentlist, add_department, remove_department



urlpatterns = [
    path('department/', departmentlist, name="list_department"),
    path('departmentlist/', departmentlist, name='departmentlist'),
    path('add_department/', add_department, name='add_department'),
    path('remove_department/<int:department_id>/', remove_department, name='remove_department'),
]


