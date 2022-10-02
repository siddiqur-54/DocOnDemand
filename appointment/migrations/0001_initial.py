# Generated by Django 3.2.7 on 2022-10-02 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('post_date', models.DateField()),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=200, null=True)),
                ('deadline', models.DateField()),
                ('fee', models.CharField(max_length=50, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('patient', models.ManyToManyField(to='patient.Patient')),
            ],
        ),
    ]
