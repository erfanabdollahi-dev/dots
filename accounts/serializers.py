from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate




#register
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'birthDate', 'image', 'image_url', 'password', 'is_staff', 'is_active']


    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('is_active', None)
        user = User.objects.create_user(password=password, is_active=True, **validated_data)
        return user