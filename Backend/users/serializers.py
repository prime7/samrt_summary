from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from users.models import User,Profile


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, data):
        password1 = data['password1']
        password2 = data['password2']
        username = data['username']

        if(password1 != password2):
            raise serializers.ValidationError({"error": "Password did not match"})

        if(User.objects.filter(username=username).exists()):
            raise serializers.ValidationError({"error": "This username is already registered"})

        return data

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password1']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        try:
            User.objects.get(username=data['username'])
        except ObjectDoesNotExist:
            raise serializers.ValidationError("User is not register")

        user = authenticate(**data)
        if user is None:
            raise serializers.ValidationError("Please check username and password")
        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated by admin')

        return user


