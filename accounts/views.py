from django.shortcuts import render
from rest_framework.views import APIView
from django.conf import settings
from .serializers import UserSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import *
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.



class UserListAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        ser = UserSerializer(users, many=True,context={'request': request})
        return Response(ser.data)


class UserDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, username):
        user = get_object_or_404(User, username=username,)
        ser = UserSerializer(user,context={'request': request})
        return Response(ser.data)
    
class Regiseter(APIView):
    def post(self,request):
        username = request.data.get('username')
        print(username)
        if User.objects.filter(username=username).exists():
          
            return Response(
                {"message": "این نام کاربری قبلاً ثبت شده است"},
                status=HTTP_400_BAD_REQUEST
            )
        ser = UserSerializer(data=request.data, context={'request': request})
        if ser.is_valid():
            user = ser.save()

            refresh = RefreshToken.for_user(user)

            return Response({'user': ser.data, 'refresh': str(refresh), 'access': str(refresh.access_token)}
                            ,status=HTTP_201_CREATED)
        

        return Response(ser.errors, status=HTTP_400_BAD_REQUEST)