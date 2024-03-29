from django.urls import path
from . import views


app_name = 'staff'
urlpatterns = [
    path('registration/', views.StaffRegistrationPage.as_view(), name='staff_reg'),
    path('dashboard/', views.StaffDetailView.as_view(), name='staff_detail'),
    path('staff_list/', views.StaffListView.as_view(), name='staff_list'),
]