from urllib import response
from django.shortcuts import render
from rest_framework import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from login.models import User
from login.serializers import UserSerializer

@api_view(['GET'])
def api_stark(request,*args,**kwrags):
    instance=User.objects.all().order_by('?').first()
    data={}
    if instance:
        data=UserSerializer(instance).data
        return Response(data)
    
@api_view(['POST'])
def api_stark(request,*args,**kwargs):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      return Response(serializer.data)
    return Response({"invalid":"not gd data"},status=400)
        
