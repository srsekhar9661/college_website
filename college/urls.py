from django.urls import path
from college import views

app_name = 'college'
urlpatterns = [
    path('index/', views.IndexPage.as_view(), name='index'),
    path('departments/', views.DepartmentList.as_view(), name='depts'),
    path('<str:dept>/department/', views.DepartmentStudentView.as_view(), name='d_std'),



    path('download-users-csv/', views.download_user_details_csv, name='download_users_csv'),
    path('browse_csv/', views.browse_csv, name='browse_csv'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
]