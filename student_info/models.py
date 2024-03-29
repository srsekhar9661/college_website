from django.db import models
from auth_app.models import MyUser


class Department(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.code
    

class StudentApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    ssc = models.FloatField()
    intermediate = models.IntegerField()
    department = models.ForeignKey(Department, on_delete = models.SET_NULL, blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.email}"


Nationality_Choices = (
    ('IND', 'India'),
    ('USA', 'United States of America'),
)


GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('Other', 'Transgender'),
)


class StudentProfile(models.Model):
    gender = models.CharField(max_length=5,choices = GENDER)
    dob = models.DateField()
    nationality = models.CharField(max_length=5, choices = Nationality_Choices)
    profile_pic = models.ImageField(upload_to='Student Profiles')
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    application = models.OneToOneField(StudentApplication, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
    