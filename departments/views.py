from django.shortcuts import render, redirect
from .models import Department
from .forms import DepartmentForm


# Create your views here.
def departmentlist(request):
    departments = Department.objects.all()
    return render(request, 'department.html', {'departments': departments})

def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departmentlist') 
    else:
        form = DepartmentForm()

    return render(request, 'add_department.html', {'form': form})



#def departmentlist(request):
 #   return render(request, 'department.html')
