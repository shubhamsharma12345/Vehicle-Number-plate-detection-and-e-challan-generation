# Generated by Django 2.2.6 on 2019-11-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('numberplatedetection', '0002_challan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challan',
            name='numberplate',
            field=models.CharField(max_length=100),
        ),
    ]
