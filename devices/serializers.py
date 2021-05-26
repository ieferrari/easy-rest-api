from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class SensorBooleanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorBoolean
        fields = '__all__'# ('pk','label','value',)

class SensorIntSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorInt
        fields = '__all__'# ('pk','label','value',)

class SensorFloatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorFloat
        fields =  '__all__'# ('pk','label','value',)






class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
