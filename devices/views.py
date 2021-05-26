from rest_framework import generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from django.contrib.auth.models import User


from django.shortcuts import render


class MyDevices(APIView):
    def get(self, request):
        a=User.objects.get(pk=1) #replace with actual user !!! TO_DO
        devices= Device.objects.filter(user=a)
        data = DeviceSerializer(devices, many=True).data
        return Response(data)


class DeviceInfo(APIView):
    def get(self, request, device_id):
        device = Device.objects.get(pk=device_id)

        sensors_boolean =SensorBoolean.objects.filter(device=device)
        sensors_boolean_data = SensorBooleanSerializer(sensors_boolean, many=True).data

        sensors_int = SensorInt.objects.filter(device=device)
        sensors_int_data = SensorIntSerializer(sensors_int, many=True).data

        sensors_float = SensorFloat.objects.filter(device=device)
        sensors_float_data = SensorIntSerializer(sensors_float, many=True).data

        return Response({'boolean_sensors':sensors_boolean_data,
                         'int_sensors:':sensors_int_data,
                         'float_sensors:':sensors_float_data})


class DeviceSensors(APIView):
    def get(self, request, device_id):
        a=User.objects.get(pk=1) #replace with actual user !!! TO_DO
        sensors = SensorBoolean.objects.filter(device=device_id)
        data = SensorBooleanSerializer(sensors, many=True).data
        return Response(data)


class GetBooleanValue(APIView):
    def get(self, request, device_id, sensor_id):
        sensor = SensorBoolean.objects.get(pk=sensor_id)
        data = SensorBooleanSerializer(sensor).data
        return Response(data)

class GetIntValue(APIView):
    def get(self, request, device_id, sensor_id):
        sensor = SensorInt.objects.get(pk=sensor_id)
        data = SensorIntSerializer(sensor).data
        return Response(data)

class GetFloatValue(APIView):
    def get(self, request, device_id, sensor_id):
        sensor = SensorFloat.objects.get(pk=sensor_id)
        data = SensorFloatSerializer(sensor).data
        return Response(data)


class SetBooleanValue(APIView):
    def post(self, request, device_id, sensor_id):
        sensor = SensorBoolean.objects.get(pk=sensor_id)
        value = request.data.get("value")   #part of the post parameters
        sensor_serializer = SensorBooleanSerializer(instance=sensor, data={
                                'value':value,
                                'label':sensor.label,
                                'device':sensor.device.pk})
        if sensor_serializer.is_valid():
            sensor_serializer.save()
            return Response(sensor_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(sensor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SetIntValue(APIView):
    def post(self, request, sensor_id):
        sensor = Sensor.objects.filter(pk=sensor_id)
        value = request.data.get("value")     #part of the post parameters
        serializer = SensorIntSerializer(intance= sensor, data={
                                'value':value,
                                'label':sensor.label,
                                'device':sensor.device.pk})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class SetFloatValue(APIView):
    def post(self, request, sensor_id):
        sensor = Sensor.objects.filter(pk=sensor_id)
        value = request.data.get("value")     #part of the post parameters
        serializer = SensorFloatSerializer(intance= sensor, data={
                                'value':value,
                                'label':sensor.label,
                                'device':sensor.device.pk})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class AddDevice(APIView):
    def post(self, request):
        user=request.user.pk
        label = request.data.get("label")
        description = request.data.get("description")
        if label==None:
            return Response({"error": "must specify a label"}, status=status.HTTP_400_BAD_REQUEST)
        data={"user":user,"label":label}
        if description !=None:
            data.uptade({"description":description,})
        serializer = DeviceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "incorrect data"}, status=status.HTTP_400_BAD_REQUEST)


class AddSensorBoolean(APIView):
    def post(self, request, device_id):
        user=request.user.pk
        device=Devices.objects.get(pk=device_id)
        if device.user.pk != user:
            return Response({"error": "user does not own this device"}, status=status.HTTP_400_BAD_REQUEST)
        label = request.data.get("label")
        if label==None:
            return Response({"error": "must specify a label"}, status=status.HTTP_400_BAD_REQUEST)
        data={"user":user, "label":label}
        value = request.data.get("value")
        if value != None:
            data.update({"value":value})
        description = request.data.get("description")
        if description !=None:
            data.uptade({"description":description,})
        serializer=SensorBooleanSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "incorrect data"}, status=status.HTTP_400_BAD_REQUEST)

class AddSensorInt(APIView):
    def post(self, request, device_id):
        user=request.user.pk
        device=Devices.objects.get(pk=device_id)
        if device.user.pk != user:
            return Response({"error": "user does not own this device"}, status=status.HTTP_400_BAD_REQUEST)
        label = request.data.get("label")
        if label==None:
            return Response({"error": "must specify a label"}, status=status.HTTP_400_BAD_REQUEST)
        data={"user":user, "label":label}
        value = request.data.get("value")
        if value != None:
            data.update({"value":value})
        description = request.data.get("description")
        if description !=None:
            data.uptade({"description":description,})
        serializer=SensorIntSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "incorrect data"}, status=status.HTTP_400_BAD_REQUEST)

class AddSensorFloat(APIView):
    def post(self, request, device_id):
        user=request.user.pk
        device=Devices.objects.get(pk=device_id)
        if device.user.pk != user:
            return Response({"error": "user does not own this device"}, status=status.HTTP_400_BAD_REQUEST)
        label = request.data.get("label")
        if label==None:
            return Response({"error": "must specify a label"}, status=status.HTTP_400_BAD_REQUEST)
        data={"user":user, "label":label}
        value = request.data.get("value")
        if value != None:
            data.update({"value":value})
        description = request.data.get("description")
        if description !=None:
            data.uptade({"description":description,})
        serializer=SensorFloatSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "incorrect data"}, status=status.HTTP_400_BAD_REQUEST)

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


from django.contrib.auth import authenticate
class LoginView(APIView):
    permission_classes = ()
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
