from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['date']
        fields = ['employnumber', 'name', 'surnames', 'birthdate', 'address', 'date_of_entry', 'department', 'date', 'photo']
        labels = {
            'employnumber': 'Número de Empleado',
            'name': 'Nombre',
            'surnames': 'Apellidos',
            'birthdate': 'Fecha de Nacimiento',
            'address': 'Dirección',
            'date_of_entry': 'Fecha de Ingreso',
            'department': 'Departamento',
            'date': 'Fecha',
            'photo': 'Foto',
        }
        
        