from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ["date"]
        widgets = {
            "employnumber": forms.TextInput(attrs={"type": "number"}),
            "name": forms.TextInput(attrs={"type": "text"}),
            "surnames": forms.TextInput(attrs={"type": "text"}),
            "birthdate": forms.DateInput(attrs={"type": "date"}),
            "address": forms.TextInput(attrs={"type": "text"}),
            "date_of_entry": forms.DateInput(attrs={"type": "date"}),
            "date": forms.DateInput(attrs={"type": "date"}),
            "photo": forms.FileInput(attrs={"type": "file"}),
        }
        # fields = ['employnumber', 'name', 'surnames', 'birthdate', 'address', 'date_of_entry', 'department', 'date', 'photo']
        # labels = {
        #     'employnumber': 'Número de Empleado',
        #     'name': 'Nombre',
        #     'surnames': 'Apellidos',
        #     'birthdate': 'Fecha de Nacimiento',
        #     'address': 'Dirección',
        #     'date_of_entry': 'Fecha de Ingreso',
        #     'department': 'Departamento',
        #     'date': 'Fecha',
        #     'photo': 'Foto',
        # }
