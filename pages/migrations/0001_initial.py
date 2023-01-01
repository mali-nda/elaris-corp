# Generated by Django 4.1.1 on 2022-09-20 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=10000)),
                ('category', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('job_type', models.CharField(max_length=200)),
                ('creation_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default='', max_length=200)),
                ('applicant_email', models.EmailField(max_length=100)),
                ('applicant_name', models.CharField(max_length=200)),
                ('applicant_phone', models.CharField(max_length=200)),
                ('resume', models.ImageField(upload_to='')),
                ('apply_date', models.DateField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.job')),
            ],
        ),
    ]