# Generated by Django 3.1.7 on 2021-04-15 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crimerec', '0008_auto_20210415_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criminalcase',
            name='crime_category',
        ),
        migrations.RemoveField(
            model_name='criminalcase',
            name='crime_district',
        ),
        migrations.RemoveField(
            model_name='criminalcase',
            name='crimedate',
        ),
        migrations.RemoveField(
            model_name='criminalcase',
            name='crimelocation',
        ),
        migrations.RemoveField(
            model_name='criminalcase',
            name='victim_name',
        ),
    ]
