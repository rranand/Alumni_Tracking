# Generated by Django 3.0 on 2020-01-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni_Tracking', '0008_auto_20200115_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='company',
            field=models.CharField(default='Unknown', max_length=50, null=True),
        ),
    ]
