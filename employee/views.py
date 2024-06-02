from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp

# Create your views here.
def home(request):
    emps = Emp.objects.all()

    return render(request, "emp/home.html", {"emps":emps})

def add_emp(request):
    if request.method == "POST":

        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        e = Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.workking = False
        else:
            e.working = True
        e.save()
        return redirect("/employee/home/")
    return render(request, "emp/addEmp.html", {})