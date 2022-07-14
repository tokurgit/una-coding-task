# Generated by Django 4.0.6 on 2022-07-14 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlucoseReading',
            fields=[
                ('user_id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('device', models.CharField(help_text='Device used to make the glucose reading', max_length=128)),
                ('serial_id', models.CharField(help_text='Serial number of the used device', max_length=64)),
                ('reading_time', models.DateTimeField(help_text='Time of the reading')),
                ('reading_type', models.IntegerField(choices=[(0, 'Zero'), (1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five'), (6, 'Six')], help_text='Type of the reading')),
                ('glucose_value', models.IntegerField(help_text='Current glucose value, mg/dL', null=True)),
                ('glucose_scan', models.IntegerField(help_text='Current glucose scan value, mg/dL', null=True)),
            ],
        ),
    ]