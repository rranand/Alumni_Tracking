# Generated by Django 3.0 on 2020-01-16 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni_Tracking', '0014_auto_20200117_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='Alumni_Tracking.comments'),
        ),
    ]
