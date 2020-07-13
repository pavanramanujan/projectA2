from django.db import models
import datetime
class CourseModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date(2020,7,6))
    time = models.TimeField()
    fee = models.FloatField()
    duration = models.IntegerField()

class StudentModel(models.Model):
    name = models.CharField(max_length=100)
    cno = models.IntegerField()
    mail = models.EmailField()
    pas = models.CharField(max_length=40)
