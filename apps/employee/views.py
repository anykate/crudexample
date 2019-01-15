from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee
from django.shortcuts import redirect, get_object_or_404


# Create your views here.
def index(request):
    employees = Employee.objects.all()
    return render(request, 'employee/index.html', {'employees': employees})


def add(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('employee_app:index')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'employee/add.html', {'form': form})


def edit(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        try:
            form.save()
            return redirect('employee_app:index')
        except:
            pass
    return render(request, 'employee/edit.html', {'employee': employee})


def delete(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    try:
        employee.delete()
    except:
        pass
    return redirect('employee_app:index')
