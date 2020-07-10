from django.shortcuts import render,redirect
from appA2.models import CourseModel
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

def admin1(request):
    return render(request,"admin1.html")


def admin_login(request):
    us = request.POST.get("a1")
    pas =request.POST.get("a2")
    if us=="pavan" and pas=="pavan":
        return render(request,"admin_page.html")
    else:
        redirect('admin1')


def schedule_class(request):
    return render(request,"schedule_class.html")


def schedule_class_reg(request):
    na = request.POST.get("s1")
    fa = request.POST.get("s2")
    da = request.POST.get("s3")
    ti = request.POST.get("s4")
    fe = request.POST.get("s5")
    du = request.POST.get("s6")
    CourseModel(name=na,faculty=fa,date=da,time=ti,fee=fe,duration=du).save()
    messages.success(request,"Schedule saved successfully")
    return redirect('schedule_class')


def all_schedule(request):
    info = CourseModel.objects.all()
    return render(request,"all_schedule.html",{"data":info})