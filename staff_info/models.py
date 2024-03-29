from django.db import models
from student_info.models  import Department, Nationality_Choices
from auth_app.models import MyUser


class StaffProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete= models.CASCADE)
    profile_pic = models.ImageField(upload_to='Staff Profiles')
    dob = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    experience = models.IntegerField()
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email
