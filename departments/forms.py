from django import forms
from .models import Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department', 'description']
        labels = {
            'department': 'Nombre ',
            'description': 'Descripción ',
        }
