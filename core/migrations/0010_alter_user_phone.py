# Generated by Django 4.1.1 on 2022-10-08 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_user_email_is_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]