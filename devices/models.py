from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #device_id = models.IntegerField(blank=False, null=False)
    label = models.CharField(blank=False, max_length=50)
    description = models.CharField(blank=True, max_length=200)
    last_connection = models.DateField( auto_now=True)
    def __str__(self):
        return str(self.pk)

tipos_de_sensor=((1,'si/no'),(2,'entero'),(3,'punto flotante'),(4,'si/no linea de tiempo'),(5,'entero linea de tiempo'),(6,'punto flotante  linea de tiempo'),)

class SensorBoolean(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    label = models.CharField(blank=False, max_length=50)
    description = models.CharField(blank=True, max_length=200)
    value  = models.BooleanField(null=True)
    def __str__(self):
        return str(self.value)

class SensorInt(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    label = models.CharField(blank=False, max_length=50)
    description = models.CharField(blank=True, max_length=200)
    value  = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return str(self.value)

class SensorFloat(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    label = models.CharField(blank=False, max_length=50)
    description = models.CharField(blank=True, max_length=200)
    value  = models.FloatField(blank=True, null=True)
    def __str__(self):
        return str(self.value)

class SensorLogger(models.Model):   #float only
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    label = models.CharField(blank=False, max_length=50)
    description = models.CharField(blank=True, max_length=200)
    def __str__(self):
        return str(self.pk)

class LogEntry(models.Model):
    sensor = models.ForeignKey(SensorLogger, on_delete=models.CASCADE)
    value = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=False, default=datetime.datetime.now)
    def __str__(self):
        return str(self.value)+' '+str(self.timestamp)
