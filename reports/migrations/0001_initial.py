# Generated by Django 4.1.1 on 2023-01-25 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('blood_group', models.CharField(blank=True, choices=[('O-', 'O-'), ('O+', 'O+'), ('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+')], max_length=3)),
                ('blood_count', models.PositiveIntegerField(default=0)),
                ('weight', models.FloatField(default=0.0)),
                ('blood_pressure', models.PositiveIntegerField(default=0)),
                ('age', models.PositiveIntegerField(default=0)),
                ('blood_donation_quantity', models.PositiveIntegerField(default=0)),
                ('donation_time', models.TimeField()),
                ('donation_date', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('donation_center', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='donation_center', to=settings.AUTH_USER_MODEL)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_donor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
