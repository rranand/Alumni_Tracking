# Generated by Django 3.0.3 on 2020-02-16 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni_Tracking', '0033_message_model'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='message_model',
            unique_together={('sender', 'receive')},
        ),
    ]
