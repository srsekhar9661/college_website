from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from .forms import StudentApplicationForm, StudentRegistrationForm, StudentProfileForm
from auth_app.forms import UserForm
from .models import StudentApplication, StudentProfile, Department, GENDER, Nationality_Choices
from auth_app.models import MyUser
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from .mixins import StudentRegistrationMixin
from django.views.generic import ListView
# from django.views.generic.detail import SingleObjectMixin
from django.views import View
from staff_info.models import StaffProfile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from auth_app.mixins import StudentLoginRequiredMixin


# class LoginRequiredMixin(object):
#     @classmethod
#     def as_view(cls):
#         return login_required(super(LoginRequiredMixin, cls).as_view())

class StudentApplicationPage(CreateView):
    model = StudentApplication
    form_class = StudentApplicationForm
    template_name = 'student_info/application_form.html'
    success_url = reverse_lazy('college:index')


class StudentRegistrationPage( StudentRegistrationMixin ,FormView):
    form_class = StudentRegistrationForm 
    template_name = 'student_info/registration_form.html'

    def get_context_data(self, *args, **kwargs):
        """
        Getting the context from the super class and adding additional content of
        Nationality Gender choices for the select tag
        """
        context_data = super().get_context_data(*args, **kwargs)
        context_data['nationality'] = Nationality_Choices
        context_data['gender'] = GENDER
        return context_data
    
    def form_valid(self, form):
        """
        After validating the form creating student_profile by sending the form data and request to the 
        StudentRegistrationMixin => create_stu_profile(request, form) 
        """
        # import ipdb;ipdb.set_trace(context=15)
        self.create_stu_profile(self.request, form)
        return redirect(reverse('college:index'))
    

# @method_decorator(login_required(login_url=reverse('authentication:stu_login')), name='dispatch')
class StudentDashboard(StudentLoginRequiredMixin,View):
    
    
    def get(self, request):
        context = {'profile':StudentProfile.objects.get(user=request.user)}
        print(context)
        return render(request, 'student_info/dashboard.html', context=context)
    
    
# @method_decorator(login_required(login_url=reverse('authentication:stu_login')), name='dispatch')
class StudentListView(ListView):
    model = StudentProfile
    template_name = 'student_info/dept_students.html'
    context_object_name = 'students'

    def get_queryset(self):
        return self.model.objects.filter(application__department__code = self.kwargs['dept'])
    


# @method_decorator(login_required(login_url=reverse('authentication:stu_login')), name='dispatch')
class StaffList(View):
    def get(self, *args, **kwargs):
        staff = StaffProfile.objects.filter(department__code=kwargs['dept'])
        return render(self.request, 'student_info/d_staff.html', {'staff_list':staff})


def success(request):
    print('*'*50)
    print(request.POST)
    print('*'*50)
    print(request.FILES)
    print('*'*50)
    return HttpResponse('Success')
        