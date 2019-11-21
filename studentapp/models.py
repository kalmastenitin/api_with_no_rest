from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.IntegerField()
    marks = models.IntegerField()
    teacher = models.CharField(max_length=50)
    f_subject = models.CharField(max_length=50)
