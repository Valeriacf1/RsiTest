from django.shortcuts import  render,redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from datetime import datetime
from django.contrib import messages

# Create your views here.

def list_employee(request):
    employees = Employee.objects.all().order_by('-date_of_entry')
    context = {'employees': employees}
    return render(request, 'employees/listEmployee.html', context)


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employeenumber = form.cleaned_data['employnumber']
            if Employee.objects.filter(employnumber=employeenumber).exists():
                messages.error(request, 'El numero de empleado ya existe. Por favor, elige otro numero.')
            else:
                form.save()
                return redirect('list_employee')
    else:
        form = EmployeeForm()

    context = {'form': form}
    return render(request, 'employees/add_employees.html', context)


def remove_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        employee.delete()
        return redirect('list_employee')

    context = {'employee': employee}
    return render(request, 'employees/remove_employee.html', context)


#def employeelist(request):
 #   return render(request, 'listEmployee.html')