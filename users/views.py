
from django.db.models import query
from rest_framework import request, viewsets
from rest_framework.response import Response
from users.serializers import RegistrationSerializer,  UserSerializer
from rest_framework.decorators import action
from django.db.models import Q
from .models import User



class UserRegistrationViewSet(viewsets.ModelViewSet ):
    serializer_class = RegistrationSerializer
    http_method_names = ['post','get','delete']
    queryset = User.objects.all()
    
    
    def create(self, request, *args, **kwargs):
        data = {}
        if request.method =="POST":
                serializer = RegistrationSerializer(data=request.data)
                if serializer.is_valid():
                    user = serializer.save()
                    data['response'] = "successfully registered"
                    data['name'] = user.username
                    data['email'] = user.email
                else:
                    data = serializer.errors
        return Response(data)
   

        



class UserIDViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    http_method_names = ['get']

    
    def get_queryset(self):
        queryset = User.objects.all()
        if self.request.query_params.get("search", None):
                search = self.request.query_params.get("search", None)
                products = queryset.filter(Q(userid__icontains=search))
                return products
    
