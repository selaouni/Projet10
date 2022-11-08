from django.shortcuts import render
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from .serializers import UserSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UserByProjectView(generics.CreateAPIView):
    queryset = User.objects.all()
    # project_id = self.request.GET.get('project_id')
    # if project_id is not None:
    #     queryset = queryset.filter(project_id=project_id)
    # return queryset
