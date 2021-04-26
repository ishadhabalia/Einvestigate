# Generated by Django 3.1.7 on 2021-03-22 01:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addcases', '0009_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextEvidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edit_id', models.CharField(max_length=3)),
                ('edit_title', models.CharField(max_length=500)),
                ('edit_content', models.TextField(max_length=5000)),
                ('edit_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('case_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='addcases.case')),
            ],
        ),
        migrations.CreateModel(
            name='FileEvidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edit_id', models.CharField(max_length=3)),
                ('edit_title', models.CharField(max_length=500)),
                ('file_name', models.CharField(max_length=500)),
                ('file_path', models.FileField(null=True, upload_to='files/', verbose_name='')),
                ('edit_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('case_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='addcases.case')),
            ],
        ),
    ]
