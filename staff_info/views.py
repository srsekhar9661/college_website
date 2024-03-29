from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import StaffRegistrationForm, StaffProfileForm
from auth_app.forms import UserForm
from student_info.models import Department
from auth_app.models import MyUser
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from .models import StaffProfile
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from auth_app.mixins import StaffLoginRequiredMixin
from django.utils.decorators import method_decorator


class StaffRegistrationPage(FormView):
    form_class = StaffRegistrationForm
    template_name = 'staff_info/staff_registration.html'

    def form_valid(self, form):
        dept = Department.objects.get(code=form.cleaned_data['department']) 
        user = UserForm(form.cleaned_data)
        if user.is_valid():
            my_user = MyUser.objects.create_user(**user.cleaned_data)
            data = form.cleaned_data
            data.pop('department')
            staff = StaffProfileForm(data, files=self.request.FILES)
            if staff.is_valid():
                # StaffProfile.objects.create(**dict(self.request.FILES),**staff.cleaned_data,user=my_user, department =dept)
                staff_profile = staff.save(commit=False)
                staff_profile.user = my_user
                staff_profile.department = dept
                staff_profile.save()
                return redirect(reverse('authentication:staff_login'))
            else:
                errors = staff.errors.as_data()
                return render(self.request, self.template_name, {'form':form, 'errors':errors})
        else:
            form.errors = user.errors
            return render(self.request, self.template_name, {'form':form})


class StaffDetailView(StaffLoginRequiredMixin, View):
    def get(self, request):
        context = {'profile':StaffProfile.objects.get(user=request.user)}
        print(context)
        return render(request, 'staff_info/dashboard.html', context=context)
    

@method_decorator(login_required(login_url=reverse_lazy('authentication:staff_login')), name='dispatch')
class StaffListView( ListView):
    model = StaffProfile
    template_name = 'staff_info/staff_list.html'
    context_object_name = 'staffs'
