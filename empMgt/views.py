from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    if request.method != "POST":
        return
    
    reqValue = request.POST.get("value")
    
    numbers = range(10)
    data = {
        "isActive": True,
        "date":datetime.datetime.now(),
        "name":"Umar Ziaii",
        "numbers": numbers,
        "value" : reqValue
    }
    return render(request, "home.html",data)

def about(request):
    # return HttpResponse("<h2>This is About Page</h2>")
    return render(request, "about.html",{})

def services(request):
    # return HttpResponse("<h2>This is Services Page</h2>")
    return render(request, "services.html",{})