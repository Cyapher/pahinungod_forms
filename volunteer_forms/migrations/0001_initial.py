from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=255)),
                ('program_img', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=13)),
                ('telephone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('birthdate', models.DateField(max_length=50)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('civilStatus', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married')], max_length=50)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other/Will not disclose', 'Other/Will not disclose')], max_length=50)),
                ('bloodType', models.CharField(max_length=3)),
                ('religion', models.CharField(max_length=50)),
                ('healthConditions', models.TextField(blank=True, null=True)),
                ('skillsHobbies', models.TextField(blank=True, null=True)),
                ('foodRestrictions', models.TextField(blank=True, null=True)),
                ('constituentUnit', models.CharField(blank=True, max_length=50, null=True)),
                ('specification', models.CharField(blank=True, max_length=50, null=True)),
                ('occupation', models.CharField(blank=True, choices=[('Physician', 'Physician'), ('Nurse', 'Nurse'), ('Pharmacist', 'Pharmacist'), ('Dentist', 'Dentist'), ('ENT', 'ENT'), ('Teacher', 'Teacher'), ('Other', 'Other')], max_length=50, null=True)),
                ('otherOccu', models.CharField(blank=True, max_length=50, null=True)),
                ('beneficiaries', models.CharField(max_length=50)),
                ('relation', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('prcLicense', models.CharField(blank=True, max_length=7, null=True)),
                ('dept', models.CharField(blank=True, max_length=50, null=True)),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('officeAdd', models.CharField(blank=True, max_length=50, null=True)),
                ('license_telephone', models.CharField(blank=True, max_length=10, null=True)),
                ('license_email', models.CharField(blank=True, max_length=50, null=True)),
                ('workSched', models.CharField(blank=True, max_length=50, null=True)),
                ('idNum', models.CharField(blank=True, max_length=50, null=True)),
                ('course', models.CharField(blank=True, max_length=50, null=True)),
                ('college', models.CharField(blank=True, max_length=50, null=True)),
                ('yearLvl', models.CharField(blank=True, choices=[('1', '1st Year'), ('2', '2nd Year'), ('3', '3rd Year'), ('4', '4th Year'), ('5', '5th Year')], max_length=1, null=True)),
                ('startDate', models.CharField(choices=[('immediately', 'Immediately'), ('next_week', 'Next Week'), ('next_month', 'Next Month'), ('Other', 'Other')], max_length=50)),
                ('customStartDate', models.DateField(blank=True, max_length=50, null=True)),
                ('programs', models.ManyToManyField(blank=True, to='volunteer_forms.program')),
            ],
        ),
    ]
