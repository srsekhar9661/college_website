from django.shortcuts import render
from .models import MyUser
from django.views.generic.edit import FormView
from.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View


class StudentLoginForm(FormView):
    form_class = LoginForm
    template_name = 'auth/login.html'

    def form_valid(self, form):
        try:
            user = authenticate(self.request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
        except MyUser.DoesNotExis:
            errors = "User doesn't exist with given credentials." 
            return render(self.request, self.template_name, {'form':form,'errors':errors})
        else:
            login(self.request, user)
            return redirect(reverse('student:stu_dashboard'))
        

class StaffLoginForm(FormView):
    form_class = LoginForm
    template_name = 'auth/login.html'

    def form_valid(self, form):
        try:
            user = authenticate(self.request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
        except MyUser.DoesNotExis:
            errors = "User doesn't exist with given credentials." 
            return render(self.request, self.template_name, {'form':form,'errors':errors})
        else:
            login(self.request, user)
            return redirect(reverse('staff:staff_detail'))


class StudentLogout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('authentication:stu_login'))


class StaffLogout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('authentication:staff_login'))