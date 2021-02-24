from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Device, Sensor, state_int, state_float


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = [ 'device_id','label','description','last_connection']

# class SensorSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model =Sensor
#         fields =['sensor_id', 'label', 'description','seconds_to_update','tipo']

class SensorSerializer(serializers.Serializer):
    #fields to serialize - deserialize
    sensor_id = serializers.IntegerField()
    label = serializers.CharField()
    description = serializers.CharField()
    seconds_to_update = serializers.IntegerField()
    tipo = serializers.IntegerField()

    # methods called to create or uptae on serializer.save()
    def create(self, validated_data):
        return Sensor.object.create(**validated_data)

    def update(self, instance, validated_data):
        instance.sensor_id = validated_data.get('sensor_id', instance.sensor_id)
        instance.label = validated_data.get('label', instance.validated_data)
        instance.description = validated_data.get('description', instance.description)
        instance.seconds_to_update = validated_data.get('seconds_to_update', instance.seconds_to_update)
        instance.tipo = validated_data.get('tipo', instance.tipo)
        instance.save()
        return instance

class StateIntSerializer(serializers.ModelSerializer):
    class Meta:
        model = state_int
        fields = [ 'state']

class StateFloatSerializer(serializers.ModelSerializer):
    class Meta:
        model = state_float
        fields = [ 'state']

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
