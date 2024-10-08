from django.shortcuts import render, redirect
from .forms import EmployeeForm

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'done.html')


    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})

def sucess(request):
    return render(request,'done.html')