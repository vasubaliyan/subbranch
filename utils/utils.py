from django.db import models
from rest_framework import permissions
from .permissions import IsStaffEditorPermission
class statusMixin(models.Model):
   created_at=models.DateTimeField(auto_now_add=True)
   updated_at=models.DateTimeField(auto_now=True)
    
class Meta:
    abstract=True
        
class StaffEditorPermissionsMixin():
   permissions_classes=[permissions,IsStaffEditorPermission]       
        