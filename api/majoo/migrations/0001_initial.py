# Generated by Django 4.2.4 on 2023-08-16 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=256, verbose_name='filename')),
                ('added_at', models.DateTimeField(auto_now_add=True, verbose_name='added_at')),
                ('status', models.IntegerField(choices=[(1, 'Needs Transcribing'), (2, 'Request Preparing'), (3, 'Request Sending'), (4, 'Request Sent'), (5, 'Done'), (6, 'Error')], default=1, verbose_name='status')),
                ('processing_start_time', models.DateTimeField(blank=True, null=True, verbose_name='processing_start_time')),
            ],
        ),
    ]