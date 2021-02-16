from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

class Device(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    device_id = models.IntegerField(blank=False, null=False)
    label = models.CharField(blank=False, max_length=50)
    description = models.CharField(blank=True, max_length=200)
    last_connection = models.DateField( auto_now=True)
    def __str__(self):
        return self.owner+str(self.device_id)

class state_boolean(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    label  = models.CharField(blank=False, max_length=50)
    state  = models.BooleanField(null=True)

class state_int(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    label = models.CharField(blank=False, max_length=50)
    state  = models.IntegerField(blank=True, null=True)

class state_float(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    label = models.CharField(blank=False, max_length=50)
    state = models.FloatField(blank=True, null=True)

class log_boolean(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    label  = models.CharField(blank=False, max_length=50)
    state  = models.BooleanField(null=True)
    timestamp = models.DateTimeField(blank=False, default=datetime.datetime.now)

class log_int(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    label = models.CharField(blank=False, max_length=50)
    state  = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=False, default=datetime.datetime.now)

class log_float(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    label = models.CharField(blank=False, max_length=50)
    state = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=False, default=datetime.datetime.now)
