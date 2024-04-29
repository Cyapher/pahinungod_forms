# Generated by Django 4.2.10 on 2024-04-22 06:49

import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer_forms', '0002_alter_authuser_date_joined_alter_authuser_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='date_joined',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='username',
            field=models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, null=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]