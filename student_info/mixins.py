from .models import StudentProfile
from auth_app.models import MyUser
from .models import StudentApplication


class StudentRegistrationMixin:
    def create_stu_profile(self,request, form):
        """
        For creating a student_profile there are two dependencies, user and application objects
        1. creating the user object by using create_user() method
        2. getting the application object using the 'email' data coming from the form.cleaned_data['email']

        info => info variable contains the data coming from both the request.POST and request.FILES in the form of dict
        details => key, value pair suitable for non-dependent fields of StudentProfile object
        """
        user = MyUser.objects.create_user(
                                    email=form.cleaned_data['email'],
                                    mobile_number=form.cleaned_data['mobile_number'],
                                    password=form.cleaned_data['password']
                                    )
        user.is_student = True
        user.save()
        application = StudentApplication.objects.get(email=form.cleaned_data['email'])
        info = dict(**request.POST, **request.FILES)
        details = {key:val[0] for key, val in info.items() if key in list(vars(StudentProfile()).keys())[1:]}
        # import ipdb; ipdb.set_trace(context=15)
        stu_profile = StudentProfile(
            user=user,
            application = application,
            **details
        )
        stu_profile.save()
        return stu_profile