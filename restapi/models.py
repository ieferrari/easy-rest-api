from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_id = models.IntegerField(blank=False, null=False)
    label = models.CharField(blank=False, max_length=50)
    description = models.CharField(blank=True, max_length=200)
    last_connection = models.DateField( auto_now=True)
    def __str__(self):
        return self.user.username+'-'+str(self.device_id)

tipos_de_sensor=((1,'si/no'),(2,'entero'),(3,'punto flotante'),(4,'si/no linea de tiempo'),(5,'entero linea de tiempo'),(6,'punto flotante  linea de tiempo'),)

class Sensor(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    sensor_id = models.IntegerField(blank=False, null=False)
    label = models.CharField(blank=False, max_length=50)
    description = models.CharField(blank=True, max_length=200)
    seconds_to_update = models.IntegerField(blank=False, null=False)
    tipo = models.IntegerField(blank=False,  choices=tipos_de_sensor)
    def __str__(self):
        return self.device.label+'-'+str(self.sensor_id)

class state_boolean(models.Model):
    sensor = models.OneToOneField(Sensor, on_delete=models.CASCADE)
    state  = models.BooleanField(null=True)

class state_int(models.Model):
    sensor = models.OneToOneField(Sensor, on_delete=models.CASCADE)
    state  = models.IntegerField(blank=True, null=True)

class state_float(models.Model):
    sensor = models.OneToOneField(Sensor, on_delete=models.CASCADE)
    state = models.FloatField(blank=True, null=True)

class log_boolean(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    state  = models.BooleanField(null=True)
    timestamp = models.DateTimeField(blank=False, default=datetime.datetime.now)

class log_int(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    state  = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=False, default=datetime.datetime.now)

class log_float(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    state = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=False, default=datetime.datetime.now)
