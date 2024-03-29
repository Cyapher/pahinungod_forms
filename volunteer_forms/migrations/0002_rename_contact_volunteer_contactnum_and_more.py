# Generated by Django 4.2.10 on 2024-03-25 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer_forms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteer',
            old_name='contact',
            new_name='contactNum',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='alumnusCheck',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='contactEmail',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='licenseCheck',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='pghCheck',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='studentCheck',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='workCheck',
            field=models.BooleanField(default=False),
        ),
    ]
