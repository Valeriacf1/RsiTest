from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
from datetime import datetime

# Create your views here.

def list_employee(request):
    employees = Employee.objects.all().order_by('-date_of_entry')
    context = {'employees': employees}
    return render(request, 'listEmployee.html', context)

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_employee')
    else:
        form = EmployeeForm()

    context = {'form': form}
    return render(request, 'listEmployee.html', context)




#def employeelist(request):
 #   return render(request, 'listEmployee.html')