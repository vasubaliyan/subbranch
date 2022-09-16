#import email
from distutils.command.upload import upload
from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField
from utils.mediapath import profile_image
from utils.utils import statusMixin

class SellerProfile(statusMixin):
    name=models.CharField(max_length=50,null=True,blank=True,default=None)
    user_name=models.CharField(max_length=50,null=True,blank=True,default=None)
    email=models.EmailField(max_length=50,unique=True)
    phone_no=models.IntegerField(blank=True)
    address_line1=models.CharField(max_length=50,blank=True,null=True,default=None)
    address_line2=models.CharField(max_length=50,blank=True,null=True,default=None)
    address_line3=models.CharField(max_length=50,blank=True,null=True,default=None)
    pin=models.CharField(max_length=20,blank=True,default=None,null=True)
    city=models.CharField(max_length=30,blank=True,null=True,default=None)
    state=models.CharField(max_length=30,blank=True,null=True,default=None)
    pic=models.ImageField(upload_to=profile_image,null=True,blank=True)
    
class BuyersProfile(statusMixin):
    name=models.CharField(max_length=100,blank=True,null=True,default=None)
    user_name=models.CharField(max_length=100,blank=True,null=True,default=None)
    email=models.EmailField(max_length=50,unique=True)
    phone_no=models.IntegerField(blank=True)
    address_line1=models.CharField(max_length=50,blank=True,null=True,default=None)
    address_line2=models.CharField(max_length=50,blank=True,null=True,default=None)
    address_line3=models.CharField(max_length=50,blank=True,null=True,default=None)
    pin=models.CharField(max_length=50,blank=True,null=True,default=None)
    city=models.CharField(max_length=50,blank=True,null=True,default=None)
    state=models.CharField(max_length=50,blank=True,null=True,default=None)
    pic=models.ImageField(upload_to=profile_image,blank=True)
    
    
    

