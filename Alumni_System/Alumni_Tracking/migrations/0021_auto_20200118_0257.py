# Generated by Django 3.0 on 2020-01-17 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni_Tracking', '0020_auto_20200118_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='verified',
            field=models.BooleanField(default=True, null=True),
        ),
    ]