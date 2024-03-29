from django import forms
from .models import StaffProfile
from auth_app.models import MyUser
from django.core.exceptions import ValidationError
from student_info.models import Department


class StaffRegistrationForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    dob = forms.DateField()
    experience = forms.CharField()
    qualification = forms.CharField()
    department = forms.ChoiceField( widget=forms.Select,
        choices = [(code[0], code[0]) for code in Department.objects.all().values_list('code')]
    )
    profile_pic =forms.ImageField()
    mobile_number = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email_data = self.cleaned_data['email']
        user_objects = MyUser.objects.all().values_list('email')
        staff = [email[0] for email in user_objects] if user_objects else []
        if email_data not in staff:
            return email_data
        else:
            raise ValidationError('Email already exists. Kindly use another email.')


class  StaffProfileForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ['profile_pic', 'dob', 'qualification', 'experience']
