# Generated by Django 3.0 on 2020-01-18 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni_Tracking', '0023_internships_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('about', models.CharField(max_length=300)),
                ('students', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=50)),
                ('money', models.CharField(max_length=20)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Alumni_Tracking.college')),
            ],
        ),
        migrations.CreateModel(
            name='fund_projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Alumni_Tracking.alumni')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Alumni_Tracking.projects')),
            ],
            options={
                'unique_together': {('ex', 'project')},
            },
        ),
    ]
