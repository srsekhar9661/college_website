from django import forms
from .models import StudentApplication, StudentProfile, GENDER, Nationality_Choices
from django.core.exceptions import ValidationError

class StudentApplicationForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        exclude = ('is_approved',)


class StudentProfileForm(forms.Form):
    gender = forms.CharField()
    dob = forms.DateField()
    nationality = forms.CharField()
    profile_pic = forms.ImageField()
    



class StudentRegistrationForm(forms.Form):
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=GENDER)
    dob = forms.DateField()
    nationality = forms.ChoiceField(choices=Nationality_Choices)
    profile_pic = forms.ImageField()
    mobile_number = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        data = self.cleaned_data['email']
        stu_applications = [ obj[0] for obj in StudentApplication.objects.all().values_list(('email'))]
        student_profiles = StudentProfile.objects.all() 
        stu_registrations = [ stu.user.email for stu in student_profiles] if student_profiles else []
        if len(stu_registrations) < 100:
            if data in stu_applications:
                student_application = StudentApplication.objects.get(email=data)
                if data not in stu_registrations:
                    if student_application.is_approved:
                        return data
                    else:
                        raise ValidationError('Your application is not approved.')
                else:
                    raise ValidationError('This email is already used.')
            else:
                raise ValidationError("Email doesn't match with your application email. Please check")
        else:
            raise ValidationError('Student Registrations are closed.')
    

class TestForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = '__all__'