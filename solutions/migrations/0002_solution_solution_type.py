# Generated by Django 3.2.9 on 2022-07-21 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='solution_type',
            field=models.CharField(choices=[('Home', 'Home'), ('Normal', 'Normal')], default='Normal', max_length=9999),
        ),
    ]
