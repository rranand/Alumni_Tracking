# Generated by Django 3.0 on 2020-01-31 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni_Tracking', '0029_file_handler'),
    ]

    operations = [
        migrations.CreateModel(
            name='public_notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('strap', models.DateTimeField(auto_now_add=True)),
                ('notice', models.CharField(max_length=300)),
            ],
        ),
    ]
