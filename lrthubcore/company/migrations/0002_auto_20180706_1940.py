# Generated by Django 2.0.7 on 2018-07-06 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Company Profile Settings'},
        ),
        migrations.RemoveField(
            model_name='company',
            name='is_deleted',
        ),
    ]