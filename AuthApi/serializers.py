from djoser.serializers import UserSerializer
from rest_framework import serializers
from .models import User
from djoser.serializers import UserSerializer

class AccountUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = '__all__'

class AccountUserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'password', 'email', 'username')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance