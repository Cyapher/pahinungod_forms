

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scope_of_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Type_obj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_code', models.CharField(max_length=5)),
                ('type_of_partnership', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=64)),
                ('partnership_extension', models.CharField(choices=[('', 'Select Partnership Extension'), ('Health Training: Basic Life Support', 'Health Training: Basic Life Support'), ('Health Training: Breast Advocacy and PFA', 'Health Training: Breast Advocacy and PFA'), ('Health Training: FAST', 'Health Training: FAST'), ('Health Education: Oral Health', 'Health Education: Oral Health'), ('Health Education: MHPS', 'Health Education: MHPS'), ('Disaster Preparedness Training', 'Disaster Preparedness Training'), ('Disaster Preparedness Lecture', 'Disaster Preparedness Lecture')], max_length=64)),
                ('stakeholder_category', models.CharField(choices=[('', 'Select Stakeholder Category'), ('Private', 'Private'), ('Government', 'Government')], max_length=64, null=True)),
                ('second_category', models.CharField(choices=[('', 'Select Second Stakeholder Category'), ('NGO', 'NGO'), ('Company', 'Company'), ('Educational Institution (Private)', 'Educational Institution (Private)'), ('LGU', 'LGU'), ('National Government Agency', 'National Government Agency'), ('Educational Institution (Government)', 'Educational Institution (Government)'), ('Others', 'Others')], max_length=64, null=True)),
                ('other_choice', models.CharField(blank=True, max_length=64)),
                ('Agreement_Start_Date', models.DateField(default=datetime.date.today)),
                ('Agreement_End_Date', models.DateField()),
                ('type_of_partnership', models.ManyToManyField(blank=True, to='partners_forms.type_obj')),
            ],
        ),
        migrations.CreateModel(
            name='Files_obj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_field', models.FileField(upload_to='partners_forms/static/partner_requirements')),
                ('file_name', models.CharField(blank=True, max_length=64, null=True)),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partner', to='partners_forms.partner')),
            ],
        ),
    ]
