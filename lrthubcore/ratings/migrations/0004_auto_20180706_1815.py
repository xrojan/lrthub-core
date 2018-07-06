# Generated by Django 2.0.7 on 2018-07-06 18:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_auto_20180706_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='value',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
