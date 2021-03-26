from django.shortcuts import render, redirect
from .models import Emp
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

# Create your views here.
def createView(request):
    return render(request,'create.html')

def store(request):
    emp = Emp()
    emp.emp_name = request.POST.get('emp_name')
    emp.emp_email = request.POST.get('emp_email')
    emp.emp_mobile = request.POST.get('emp_mobile')
    emp.save()
    messages.success(request, "Employee Added Successfully")
    return redirect('/create')

