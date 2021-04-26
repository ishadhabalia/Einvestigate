# Generated by Django 3.1.7 on 2021-04-11 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimerec', '0004_auto_20210403_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminalrecord',
            name='crime_district',
            field=models.CharField(choices=[('Ahmednagar', 'Ahmednagar'), ('Akola', 'Akola'), ('Amravati', 'Amravati'), ('Aurangabad', 'Aurangabad'), ('Beed', 'Beed'), ('Bhandara', 'Bhandara'), ('Corruption', 'Corruption'), ('Buldhana', 'Buldhana'), ('Robbery', 'Robbery'), ('Chandrapur', 'Chandrapur'), ('Dhule', 'Dhule'), ('Gadchiroli', 'Gadchiroli'), ('Gondia', 'Gondia'), ('Hingoli', 'Hingoli'), ('Jalgaon', 'Jalgaon'), ('Jalna', 'Jalna'), ('Kolhapur', 'Kolhapur'), ('Latur', 'Latur'), ('Mumbai City', 'Mumbai City'), ('Mumbai Suburban', 'Mumbai Suburban'), ('Nagpur', 'Nagpur'), ('Nanded', 'Nanded'), ('Nandurbar', 'Nandurbar'), ('Nashik', 'Nashik'), ('Osmanabad', 'Osmanabad'), ('Palghar', 'Palghar'), ('Parbhani', 'Parbhani'), ('Pune', 'Pune'), ('Raigad', 'Raigad'), ('Ratnagiri', 'Ratnagiri'), ('Sangli', 'Sangli'), ('Satara', 'Satara'), ('Sindhudurg', 'Sindhudurg'), ('Solapur', 'Solapur'), ('Thane', 'Thane'), ('Wardha', 'Wardha'), ('Washim', 'Washim'), ('Yavatmal', 'Yavatmal')], default='', max_length=30),
        ),
    ]
