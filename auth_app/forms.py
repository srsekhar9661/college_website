from django import forms
from django.core.exceptions import ValidationError


class UserForm(forms.Form):
    email = forms.EmailField()
    mobile_number = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)

    
    def clean_mobile_number(self):
        num = str(self.cleaned_data['mobile_number'])
        if num.isdigit():
            if len(num) == 10:
                if num[0] in '9876':
                    return int(num)
                else:
                    raise ValidationError('Mobile Number must always start with 9, 8, 7, or 6.')
            else:
                raise ValidationError('Number must be 10 digits only.')
        else:
            raise ValidationError('Mobile Number consistes of 10 digits only. Please enter a Valid Mobile Number')


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        passwd = self.cleaned_data['password']
        if len(passwd)>=8:
            return passwd
        else:
            raise ValidationError('Password must be atleast 8 characters.')
        

