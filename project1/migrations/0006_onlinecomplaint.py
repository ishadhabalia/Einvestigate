# Generated by Django 3.1.7 on 2021-11-28 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0005_auto_20210322_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineComplaint',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('complainant_name', models.CharField(default='', max_length=100)),
                ('complainant_contact', models.CharField(blank=True, max_length=10)),
                ('complainant_email', models.EmailField(default='', max_length=50)),
                ('complainant_address', models.TextField()),
                ('complaint', models.TextField()),
                ('crime_district', models.CharField(choices=[('Select district', 'Select district'), ('Ahmednagar', 'Ahmednagar'), ('Akola', 'Akola'), ('Amravati', 'Amravati'), ('Aurangabad', 'Aurangabad'), ('Beed', 'Beed'), ('Bhandara', 'Bhandara'), ('Buldhana', 'Buldhana'), ('Chandrapur', 'Chandrapur'), ('Dhule', 'Dhule'), ('Gadchiroli', 'Gadchiroli'), ('Gondia', 'Gondia'), ('Hingoli', 'Hingoli'), ('Jalgaon', 'Jalgaon'), ('Jalna', 'Jalna'), ('Kolhapur', 'Kolhapur'), ('Latur', 'Latur'), ('Mumbai City', 'Mumbai City'), ('Mumbai Suburban', 'Mumbai Suburban'), ('Nagpur', 'Nagpur'), ('Nanded', 'Nanded'), ('Nandurbar', 'Nandurbar'), ('Nashik', 'Nashik'), ('Osmanabad', 'Osmanabad'), ('Palghar', 'Palghar'), ('Parbhani', 'Parbhani'), ('Pune', 'Pune'), ('Raigad', 'Raigad'), ('Ratnagiri', 'Ratnagiri'), ('Sangli', 'Sangli'), ('Satara', 'Satara'), ('Sindhudurg', 'Sindhudurg'), ('Solapur', 'Solapur'), ('Thane', 'Thane'), ('Wardha', 'Wardha'), ('Washim', 'Washim'), ('Yavatmal', 'Yavatmal')], default='', max_length=30)),
                ('crime_location', models.CharField(max_length=100)),
            ],
        ),
    ]