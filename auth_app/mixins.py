from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class StaffLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('authentication:staff_login')


class StudentLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('authentication:stu_login')
