from django.contrib import admin
from .models import StudentApplication, StudentProfile, Department


class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = ['name', 'code']


admin.site.register(Department, DepartmentAdmin)


class StudentApplicationAdmin(admin.ModelAdmin):
    model = StudentApplication
    list_display = ['name', 'email', 'ssc', 'intermediate', 'department', 'is_approved']

admin.site.register(StudentApplication, StudentApplicationAdmin)
admin.site.register(StudentProfile)
