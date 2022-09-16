from django.shortcuts import render
from.serializers import SellerProfileSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.views import APIView
#from utils.permissions import IsStaffEditorPermission
#from utils.mixin import StaffEditorPermissionMixin
from.models import SellerProfile,BuyersProfile
from django.http import Http404

#class SellerProfileListCreateAPIViewe(generics.ListCreateAPIView):
 #   queryset=SellerProfile.objects.all()
  #  serializer_class=SellerProfileSerializer
    #permission_classes=[permissions.DjangoModelPermissions]
    #permissions_classes=[permissions.IsAdminUser,IsStaffEditorPermission]
    #authentication_classes=[ISauthentication]
    
    #def perform_create(self, serializer,request:Request):
     #   data=request.data
      #  serializer=self.serializer_class(data=data)
       # if serializer.is_valid():
        #    serializer.save()
         #   response={"message":"profile created sucessfully","data":serializer.data}
          #  return Response(data=response,status=status.HTTP_201_CREATED)
        #return Response(data=serializer.errors,status=status.HTTP_404_BAD_REQUEST)
        
    #def perform_create(self, serializer):
       # return super().perform_create(serializer)    
        
    
        #return super().perform_create(serializer)  
class SellerProfileAPI(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            pro=SellerProfile.objects.get(id=id)
            serializer=SellerProfileSerializer(pro)
            return Response(serializer.data)
        pro=SellerProfile.objects.all()
        serializer=SellerProfileSerializer(pro,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer=SellerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"data created sucessfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)
    
    def put(self,request,pk,format=None):
        id=pk
        pro=SellerProfile.objects.get(pk=id)
        serializer=SellerProfileSerializer(pro,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"data complet update"})
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    def patch(self,request,pk,format=None):
        id=pk
        pro=SellerProfile.objects.get(pk=id)
        serializer=SellerProfileSerializer(pro,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"partially data update"})
        return Response(serializer.errors)
    def delete(self,request,pk,format=None):
        id=pk
        pro=SellerProfile.objects.get(pk=id)
        pro.delete()
        return Response({"msg":"data delete"})
            
#Profile_list_view=SellerProfileAPI.as_view()    


#class SellerProfileDetailAPIView(generics.RetrieveAPIView):
 #   queryset=SellerProfile.objects.all()
  #  serializer_class=SellerProfileSerializer
   # lookup_field="pk"
    #SellerProfile.objects.get(pk=1)

#Profile_detail_view=SellerProfileDetailAPIView.as_view()

#class SellerProfileUpdateAPIView(generics.UpdateAPIView):
 #   queryset=SellerProfile.objects.all()
  #  serializer_class=SellerProfileSerializer
   # lookup_field="pk"
    
    #def perform_update(self, serializer):
     #   return super().perform_update(serializer)
        
        
        #return super().perform_update(instance)     
#Profile_update_view=SellerProfileUpdateAPIView.as_view()



#class SellerProfileDestroyAPIView(generics.DestroyAPIView):
 #   queryset=SellerProfile.objects.all()
  #  serializer_class=SellerProfileSerializer
   #lookup_field="pk"

    #def destroy(self,instance):
     #   return super().destroy(instance)
    
#Profile_destroy_view=SellerProfileDestroyAPIView.as_view()    