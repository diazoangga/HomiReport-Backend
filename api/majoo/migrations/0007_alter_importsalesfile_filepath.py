# Generated by Django 4.2.4 on 2023-08-18 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majoo', '0006_alter_importsalesfile_filepath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importsalesfile',
            name='filepath',
            field=models.CharField(default=None, max_length=256, null=True, verbose_name='filepath'),
        ),
    ]
