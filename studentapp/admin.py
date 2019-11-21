from django.contrib import admin
from studentapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rollno', 'marks', 'teacher','f_subject']

admin.site.register(Student,StudentAdmin)
