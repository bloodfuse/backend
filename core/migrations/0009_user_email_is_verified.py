# Generated by Django 4.1.1 on 2022-10-08 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_user_first_name_alter_user_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
