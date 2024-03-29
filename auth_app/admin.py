from django.contrib import admin
from .models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    model = MyUser
    list_display = ['email', 'mobile_number', 'is_staff', 'is_admin', 'date_joined', 'is_student']


admin.site.register(MyUser, MyUserAdmin)

