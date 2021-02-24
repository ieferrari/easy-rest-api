from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions, generics
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from restapi.models import Device, Sensor, state_boolean, state_int, state_float, log_boolean, log_int, log_float
from restapi.serializers import UserSerializer, GroupSerializer, DeviceSerializer, SensorSerializer, StateIntSerializer, StateFloatSerializer

def inicio_view(request):
    return render(request, 'index.html')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Device.objects.filter(user=user)

@csrf_exempt  #este exempt es para el post.. quitar!
def Device_list(request):
    ''' list all Devices '''
    if request.method == 'GET':
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif  request.method == 'POST':
        data = JSONPasrser().parse(request)
        serializser = DeviceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def my_devices(request):
    devices = Device.objects.filter(user=request.user)


def get_device_info(request, device_id):
    try:
        device = Device.objects.get(pk=device_id)
    except device.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = DeviceSerializer(device)
        return JsonResponse(serializer.data)

@csrf_exempt
def get_sensor_info(request, sensor_id, device_id):
    user = request.user
    try:
        device = Device.objects.filter(user=user).get(device_id=device_id)
    except Device.DoesNotExist:
        print('device not found')
        return HttpResponse(status=404)
    try:
        sensor = Sensor.objects.filter(device=device).get(sensor_id=1)
    except Sensor.DoesNotExist:
        print('sensor not found')
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = DeviceSerializer(sensor)
        return JsonResponse(serializer.data)


def get_sensor_value(request, sensor_id, device_id):
    try:
        device = Device.objects.filter(user=request.user).get(device_id=device_id)
    except Device.DoesNotExist:
        print('device not found')
        return HttpResponse(status=404)
    try:
        sensor = Sensor.objects.filter(device=device).get(sensor_id=sensor_id)
    except Sensor.DoesNotExist:
        print('sensor not found')
        return HttpResponse(status=404)
    if request.method == 'GET':
        state=state_int.objects.get(sensor=sensor)
        serializer = StateIntSerializer(state)
        return JsonResponse(serializer.data)


def set_sensor_value(request, device_id, sensor_id, value):
    user = request.user
    try:
        device = Device.objects.filter(user=user).get(device_id=device_id)
    except Device.DoesNotExist:
        print('device not found')
        return HttpResponse(status=404)
    try:
        sensor = Sensor.objects.filter(device=device).get(sensor_id=sensor_id)
    except Sensor.DoesNotExist:
        print('sensor not found')
        return HttpResponse(status=404)

    if request.method == 'GET':
        try:
            state=state_int.objects.get(sensor=sensor)
            state.state=value
            state.save()
        except state_int.DoesNotExist:
            state=state_int(sensor=sensor, state=value)
            state.save()
        serializer = StateIntSerializer(state)
        return JsonResponse(serializer.data)

def change_float(request, device_id, sensor_id, value):
    user = request.user
    try:
        device = Device.objects.filter(user=user).get(device_id=device_id)
    except Device.DoesNotExist:
        print('device not found')
        return HttpResponse(status=404)
    try:
        sensor = Sensor.objects.filter(device=device).get(sensor_id=1)
    except Sensor.DoesNotExist:
        print('sensor not found')
        return HttpResponse(status=404)

    if request.method == 'GET':
        state=state_float(sensor=sensor, state=value)
        state.save()
        print("guardado")
        serializer = StateFloatSerializer(state)
        return JsonResponse(serializer.data)


def log_value(request, device_id, sensor_id, value, timestamp):
    user = request.user
    try:
        device = Device.objects.filter(user=user).get(device_id=device_id)
    except Device.DoesNotExist:
        print('device not found')
        return HttpResponse(status=404)
    try:
        sensor = Sensor.objects.filter(device=device).get(sensor_id=1)
    except Sensor.DoesNotExist:
        print('sensor not found')
        return HttpResponse(status=404)

    if request.method == 'GET':
        state=log_int(sensor=sensor, state=value, timestamp=timestamp)
        state.save()
        print("guardado")
        #serializer = StateIntSerializer(state)
        return None #JsonResponse(serializer.data)




class SensorViewSet(viewsets.ModelViewSet):
    serializer_class = SensorSerializer
    permission_classes =[permissions.IsAuthenticated]
    def get_queryset(self):
        user =self.request.user
        device = self.request.query_params.get('device')
        return Sensor.objects.filter(device=device)
