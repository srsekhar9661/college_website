from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class CustomManager(BaseUserManager):
    def create_user(self, email, mobile_number, password=None):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(
            email = self.normalize_email(email),
            mobile_number = mobile_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, mobile_number, password=None):
        user = self.create_user(
            email = email,
            mobile_number = mobile_number,
            password = password
        )
        # user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)

        return user
    

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        max_length = 255,
        verbose_name = 'Email Address',
        unique = True
    )
    mobile_number = models.BigIntegerField(
        verbose_name ='Mobile Number'
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add = True)

    objects = CustomManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile_number']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin


