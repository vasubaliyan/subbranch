from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import ValidationError
from.models import User
from rest_framework.authtoken.models import Token

#class SignUpSerializer(serializers.ModelSerializer):
  # name=serializers.CharField()
  #  username=serializers.CharField()
  #  phone_no=serializers.IntegerField()
   # email=serializers.CharField()
    #password=serializers.CharField()
    #confirm_password=serializers.CharField()
    
    #class Meta:
     #   model=User
      #  fields=["name","username","phone_no","email","password","confirm_password"]

class UserSerializer(serializers.ModelSerializer):
    name=serializers.CharField()
    username=serializers.CharField()
    phone_no=serializers.IntegerField()
    email=serializers.CharField()
    password=serializers.CharField()
    confirm_password=serializers.CharField()
    class Meta:
        model=User
        fields=["name","username","phone_no","email","password","confirm_password"]
    
    def validata(self,attrs):
        email_exists=User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise ValidationError("email has alredy been used")
        return super().validate(attrs)  
        
    def create(self,validated_data):
        password=validated_data.pop("password")
        user=super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
    
