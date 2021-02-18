from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Device)
admin.site.register(Sensor)
admin.site.register(log_int)
