# Generated by Django 3.1.6 on 2021-05-27 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_devicesperuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_id', models.IntegerField(default=-1)),
                ('tipo', models.IntegerField(choices=[(1, 'SensorBoolean'), (2, 'SensorInt'), (3, 'SensorFloat')])),
                ('sensor_pk', models.IntegerField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.device')),
            ],
        ),
    ]
