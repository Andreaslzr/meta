from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.core.exceptions import PermissionDenied
from django.db.models import Q
#CONDIÇÃO POR GRUPO
#permite apenas que coordenadores façam GET/POST/PUT/DELETE
# class DeadlineCustomPermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.groups.filter(name='Coordenador').exists()

#CONDIÇÃO POR GRUPO
#permite que apenas coordenadores façam POST/PUT/DELETE
#mas libera o GET para todos os usuários autenticados
# class DeadlineCustomPermission(BasePermission):
#     def has_permission(self, request, view):
#         if request.method == 'GET':
#             return request.user.is_authenticated        
        
#         return request.user.groups.filter(Q(name='Coordenador') | Q(name='Admin')).exists()

#CONDIÇÃO POR PERMISSÃO
#todos que tiverem a permissão view podem fazer GET
#os que tiverem permissão add, delete, change deadline podem fazer GET/POST/PUT/DELETE
class DeadlineCustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.has_perm('main.view_deadline')
                
        return request.user.has_perms(['main.add_deadline','main.delete_deadline','main.change_deadline'])

#CONDIÇÃO POR PERMISSÃO
#cada método vai ser permitido de acordo com cada permissão
# class DeadlineCustomPermission(BasePermission):
#     def has_permission(self, request, view):
#         if request.method == 'GET':
#             return request.user.has_perm('main.view_deadline')
#         if request.method == 'POST':
#             return request.user.has_perm('main.add_deadline')
#         if request.method == 'DELETE':
#             return request.user.has_perm('main.delete_deadline')
#         if request.method == 'PUT':
#             return request.user.has_perm('main.change_deadline')                
#         return False


class DeadlineView(ModelViewSet):
    queryset = Deadline.objects.all()
    serializer_class = DeadlineSerializer
    permission_classes = (DeadlineCustomPermission,)
    
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.groups.filter(name='Coordenador').exists():
    #         return Deadline.objects.all()
    #     else:
    #         raise PermissionDenied()