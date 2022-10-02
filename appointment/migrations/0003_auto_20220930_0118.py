# Generated by Django 3.2.7 on 2022-09-29 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_patient_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='status',
        ),
        migrations.AddField(
            model_name='doctor',
            name='status',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
