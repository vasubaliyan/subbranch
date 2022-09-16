from dataclasses import fields
#from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from.models import *

class SellerProfileSerializer(ModelSerializer):
    
    
    class Meta:
        model=SellerProfile
        fields=["name","user_name","email","phone_no","address_line1","address_line2","address_line3","pin","city","state","pic"
        ]
        #fields="__all__"
        #exclude=["is_delete",]
        #filter_fields='__all__'
        #extra_kwargs={
         #   "":{}
        #}
        
class BuyersProfileSerializer(ModelSerializer):
    class Meta:
        model=BuyersProfile
        fields=("name","user_name","email","phone_no","address_line1","address_line2","address_line3","pin","city","state","pic")
        exclude=("is_delete",)    
