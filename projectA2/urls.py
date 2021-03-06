"""projectA2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from appA2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index , name='index'),
    path('admin1/', views.admin1, name='admin1'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('schedule_class/', views.schedule_class, name='schedule_class'),
    path('schedule_class_reg/', views.schedule_class_reg, name='schedule_class_reg'),
    path('all_schedule/', views.all_schedule, name='all_schedule'),
    path('update_course/',views.update_course, name='update_course'),
    path('update_course_conf/',views.update_course_conf,name='update_course_conf'),
    path('delete/', views.delete, name='delete'),
    path('student_home/',views.student_home,name='student_home'),
    path('student_registration/',views.student_registration,name='student_registration'),
    path('student_details/',views.student_details,name='student_details'),
    path('student_login/',views.student_login,name = 'student_login'),
    path('stu_log_conf/',views.stu_log_conf,name='stu_log_conf'),
    path('enrole_page/',views.enrole_page,name='enrole_page'),
    path('enrole_course/',views.enrole_course,name='enrole_course'),
    path('view_all_nrol_courses/',views.view_all_nrol_courses,name='view_all_nrol_courses'),
    path('remove_course/',views.remove_course,name='remove_course')
]
