# Generated by Django 3.1.7 on 2021-04-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CriminalRecords',
            fields=[
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Not Specified')], max_length=1)),
                ('crime_category', models.CharField(choices=[('R', 'Robbery'), ('CC', 'Cyber-crime'), ('DV', 'Domestic violence'), ('SA', 'Sexual Assault'), ('CA', 'Child Abuse'), ('T', 'Terrorism'), ('VC', 'Violent Crime'), ('C', 'Corruption'), ('P', 'Poaching')], max_length=2)),
                ('criminal_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('criminal_firstname', models.CharField(default='', max_length=100)),
                ('criminal_lastname', models.CharField(default='', max_length=100)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('no_of_crimes', models.PositiveSmallIntegerField(default=1)),
                ('crimedate', models.DateField(blank=True, null=True)),
                ('crimelocation', models.CharField(blank=True, max_length=30)),
                ('victim_name', models.CharField(default='', max_length=100)),
                ('crime_description', models.TextField()),
                ('jail_name', models.CharField(default='', max_length=100)),
                ('sentence_status', models.TextField(max_length=500)),
                ('crime_punishment', models.TextField()),
            ],
        ),
    ]
