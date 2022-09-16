from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import AbstractUser
class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
       email=self.normalize_email(email)     
       user=self.model(email=email,**extra_fields)
       user.user_password=password
       user.set_password(password)
       user.save()
       return user
    
    def create_superuser(self,email,password,**other_fields):
        other_fields.setdefault("is_staff",True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser has to have is_staff being True')
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser should have is_superuser as True")
        if other_fields.get("is_active") is not True:
            raise ValueError("Superuser should have is_active as True")
        return self.create_user(email=email,password=password, **other_fields)
        
class User(AbstractUser):
    name=models.CharField(max_length=100,blank=True,null=True,default=None)
    username=models.CharField(max_length=100,blank=True,null=True,default=None)
    phone_no=models.CharField(max_length=11,blank=True,null=True,default=None)
    email=models.EmailField(max_length=50,blank=True,null=True,default=None,unique=True)
    password=models.CharField(max_length=20,blank=True,null=True,default=None)
    confirm_password=models.CharField(max_length=20,blank=True,null=True,default=None)

    objects=CustomUserManager()
    USERNAME_FIELD= "email"
    REQUIRED_FIELDS=["username"]
    def __str__(self):
        return self.username
        
   