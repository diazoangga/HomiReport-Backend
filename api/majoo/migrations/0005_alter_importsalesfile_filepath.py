# Generated by Django 4.2.4 on 2023-08-18 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majoo', '0004_remove_importsalesfile_filename_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importsalesfile',
            name='filepath',
            field=models.CharField(max_length=256, verbose_name='filepath'),
        ),
    ]
