# Generated by Django 2.0.7 on 2018-07-10 09:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_feedtype_posted_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedtype',
            name='posted_date',
        ),
        migrations.AddField(
            model_name='feed',
            name='posted_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]