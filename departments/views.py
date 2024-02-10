from django.shortcuts import render, redirect, get_object_or_404
from .models import Department
from .forms import DepartmentForm


# Create your views here.
def departmentlist(request):
    departments = Department.objects.all()
    print(departments)
    return render(request, 'deparments/department.html', {'departments': departments})

def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departmentlist') 
    else:
        form = DepartmentForm()

    return render(request, 'deparments/add_department.html', {'form': form})


def remove_department(request, department_id):
    department = get_object_or_404(Department, pk=department_id)

    if request.method == 'POST':
        department.delete()
        return redirect('departmentlist')

    return render(request, 'deparments/remove_department.html', {'department': department})

    


#def departmentlist(request):
 #   return render(request, 'department.html')
