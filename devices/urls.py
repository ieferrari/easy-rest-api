from django.urls import path
from .views import *

urlpatterns = [
    path('my_devices/', MyDevices.as_view(), name='my_devices'),               #list of all your devices
    path('add_device/',AddDevice.as_view(), name='add_device' ),

    path('device/<int:device_id>/',DeviceInfo.as_view(), name='device_info' ), #list of every sensor of specific device
    path('device/<int:device_id>/add_sensor_boolean)', AddSensorBoolean.as_view(), name='add_sensor_boolean'),
    path('device/<int:device_id>/add_sensor_int)', AddSensorInt.as_view(), name='add_sensor_int'),
    path('device/<int:device_id>/add_sensor_Float)', AddSensorFloat.as_view(), name='add_sensor_float'),

    path('device/<int:device_id>/sensor/<int:sensor_id>/get_boolean/', GetBooleanValue.as_view(), name='get_boolean_for_sensor'),
    path('device/<int:device_id>/sensor/<int:sensor_id>/get_int/', GetIntValue.as_view(), name='get_int_for_sensor'),
    path('device/<int:device_id>/sensor/<int:sensor_id>/get_float/', GetFloatValue.as_view(), name='get_float_for_sensor'),

    path('device/<int:device_id>/sensor/<int:sensor_id>/set_boolean_value/', SetBooleanValue.as_view(), name='set_boolean_value'),
    path('device/<int:device_id>/sensor/<int:sensor_id>/set_int_value/', SetIntValue.as_view(), name='set_int_value'),
    path('device/<int:device_id>/sensor/<int:sensor_id>/set_float_value/', SetFloatValue.as_view(), name='set_float_value'),

    path("login/", LoginView.as_view(), name="login"),
    path("users/", UserCreate.as_view(), name="user_create"),
]
