# Generated by Django 3.0 on 2020-01-19 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni_Tracking', '0025_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_on',
            field=models.DateField(null=True),
        ),
    ]
