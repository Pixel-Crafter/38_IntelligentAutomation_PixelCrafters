from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

@login_required
def adminPage(request):
    return render(request, "adminPage.html")

@login_required
def employee_page(request):
    return render(request, 'emp.html')