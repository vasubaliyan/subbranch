from urllib import response
from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from.models import User


class UserView(generics.GenericAPIView):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    def post(self,request:Request):
        data=request.data
        
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response={"message":"user created sucessfully","data":serializer.data}
            return Response(data=response,status=status.HTTP_201_CREATED)
        return Response(data=serializer.error_messages,status=status.HTTP_404_NOT_FOUND)
    
    #def get(self,request,pk=None,*args,**kwargs):
     #   print(args,kwargs)
      #  pk=kwargs.get("pk")
       # if pk is not None:
        #    return self.retrieve(request,*args,**kwargs)
        #return self.list(request,*args,**kwargs)
        
        
    ##   user=User.objects.all()
      #  serializer=UserSerializer(user,many=True)
       # return Response(serializer.data) 
        
    
class LoginView(APIView):
    def post(self,request:Request):
        email=request.data.get("email")
        password=request.data.get("password")
        user=authenticate(email=email,password=password)
        if user is not None:
            response={
                "message":"Login Successfully",
                "token":user.auth_token.key}
            
            return Response(data=response,status=status.HTTP_200_OK)
        else:
            return Response(data={"message":"invalid email or password"})
    
    def get(self,request:Request):
        content={"user":str(request.user),
                 "auth":str(request.auth)}
        return Response(data=content,status=status.HTTP_200_OK)
        

