# Generated by Django 3.0.4 on 2020-07-09 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetail',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
