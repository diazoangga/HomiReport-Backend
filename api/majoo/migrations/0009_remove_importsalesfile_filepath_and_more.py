# Generated by Django 4.2.4 on 2023-08-18 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majoo', '0008_alter_importsalesfile_filepath'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importsalesfile',
            name='filepath',
        ),
        migrations.AddField(
            model_name='importsalesfile',
            name='filename',
            field=models.CharField(default=None, max_length=256, verbose_name='filename'),
        ),
    ]
