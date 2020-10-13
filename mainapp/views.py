import uuid

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

from mainapp.serializers import UserSerializer


# 这下展示前端配置了代理时的情况
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['post'], detail=False, authentication_classes=[SessionAuthentication],
            permission_classes=[permissions.AllowAny])
    def login(self, request):
        una = request.data.get('username')
        pwd = request.data.get('password')
        if una is not None and pwd is not None:
            islogin = authenticate(request, username=una, password=pwd)
            if islogin:
                login(request, islogin)
                token = uuid.uuid4().hex
                return Response({
                    "status": 0,
                    "message": "Login Success",
                    "username": una,
                    "token": token,
                })
            else:
                return Response({
                    "status": 1,
                    "message": "登录失败, 请检查用户名或者密码是否输入正确."
                })
        else:
            return Response({
                "status": 2,
                "message": "参数错误"
            })

    @action(methods=['get'], detail=False, authentication_classes=[SessionAuthentication],
            permission_classes=[permissions.IsAuthenticated])
    def get_all_user(self, request):
        serializer = UserSerializer(instance=self.queryset, many=True)
        return Response(serializer.data)
