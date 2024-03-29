from django.urls import path
from . import views


app_name = 'authentication'
urlpatterns = [
    path('student_login/', views.StudentLoginForm.as_view(), name='stu_login'),
    path('student_logout/', views.StudentLogout.as_view(), name='stu_logout'),
    path('staff/login/', views.StaffLoginForm.as_view(), name='staff_login'),
    path('staff/logout/', views.StaffLogout.as_view(), name='staff_logout'),
]
