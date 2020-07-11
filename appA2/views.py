from django.shortcuts import render,redirect
from appA2.models import CourseModel
from django.contrib import messages
def index(request):
    return render(request,"index.html")
def admin1(request):
    return render(request,"admin1.html")
def admin_login(request):
    us = request.POST.get("a1")
    pas =request.POST.get("a2")
    if us=="pavan" and pas=="pavan":
        return render(request,"admin_home.html")
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
def update_course(request):
    no = request.GET.get("idn")
    print(no)
    print("this is no")
    res = CourseModel.objects.get(id=no)
    print(res)
    return render(request,"update_course.html",{"info":[res]})
def update_course_conf(request):
    no = request.POST.get("u1")
    na = request.POST.get("u2")
    fa = request.POST.get("u3")
    da = request.POST.get("u4")
    ti = request.POST.get("u5")
    fe = request.POST.get("u6")
    du = request.POST.get("u7")
    CourseModel.objects.filter(id=no).update(name=na,faculty=fa,date=da,time=ti,fee=fe,duration=du)
    return redirect('all_schedule')


def delete(request):
    no = request.GET.get("idn")
    res = CourseModel.objects.get(id=no).delete()
    messages.success(request,"Requested Course Deleted Successfully")
    return redirect('all_schedule')


def admin_home(request):
    return render(request,'admin_home.html')