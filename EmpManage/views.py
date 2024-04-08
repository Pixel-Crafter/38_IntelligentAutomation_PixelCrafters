from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from.forms import EmployeeForm

def login_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']
            password = form.cleaned_data['password']
            user = authenticate(employee_id=employee_id, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = EmployeeForm()
    return render(request, 'login.html', {'form': form})

def dashboard(request):
    employee = request.user.employee
    leaves = Leave.objects.filter(employee=employee)
    context = {'employee': employee, 'leaves': leaves}
    return render(request, 'dashboard.html', context)