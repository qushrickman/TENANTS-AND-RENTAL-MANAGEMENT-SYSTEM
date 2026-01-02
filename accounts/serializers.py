from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'role')

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    
    role = serializers.ChoiceField(choices=Profile.ROLE_CHOICES,write_only=True)
    
    def create(self, validated_data):
        role = validated_data.pop('role')
        
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
            )
        
        Profile.objects.create(
            user=user,
            role=role
            )
        return user
    

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'role')
        extra_kwargs = {
            'password': {'write_only': True}
            }

    def create(self, validated_data):
        role = validated_data.pop('role')
        
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            )
        
        Profile.objects.create(
            user=user,
            role=role
            )
        return user