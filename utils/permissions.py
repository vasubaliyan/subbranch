from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map={
        'GET':['%{app_label}s.view_%{model_name}'],
        'OPTIONS':[],
        'HEAD':[],
        'POST':['%{app_label}s.add_%{model_name}'],
        'PUT':['%{app_label}s.change_%{model_name}'],
        'PATCH':['%{app_label}s.change_%{model_name}'],
        'DELETE':['%{app_label}s.delete_%{model_name}'],             
    }
    def has_permission(self, request, view):
        if not request.user.username=="vasu007":
            return False
        if not request.user.is_staff():
            return False
        return super().has_permission(request, view)
    
    