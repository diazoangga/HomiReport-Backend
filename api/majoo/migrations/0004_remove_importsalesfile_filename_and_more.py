# Generated by Django 4.2.4 on 2023-08-17 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majoo', '0003_dailysales'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importsalesfile',
            name='filename',
        ),
        migrations.AddField(
            model_name='importsalesfile',
            name='filepath',
            field=models.FileField(default=None, max_length=256, upload_to='', verbose_name='filepath'),
        ),
    ]
