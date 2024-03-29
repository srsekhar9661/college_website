from django.urls import path
from . import views


app_name = 'student'
urlpatterns = [
    path('student_application_form/', views.StudentApplicationPage.as_view(), name='stu_application_form'),
    path('student_registration/', views.StudentRegistrationPage.as_view(), name='stu_reg'),
    path('stu_dashboard/', views.StudentDashboard.as_view(), name='stu_dashboard'),
    path('<str:dept>/students/', views.StudentListView.as_view(), name='dept_students'),
    path('<str:dept>/staff/', views.StaffList.as_view(), name='staff'),
    path('success/', views.success, name='success'),

]