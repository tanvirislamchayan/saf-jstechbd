# Generated by Django 4.2.17 on 2025-01-01 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_delete_allstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsaf',
            name='regNo',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
