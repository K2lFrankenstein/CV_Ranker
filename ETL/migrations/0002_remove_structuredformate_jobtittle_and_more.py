# Generated by Django 5.0.6 on 2024-05-31 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ETL', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='structuredformate',
            name='jobTittle',
        ),
        migrations.RemoveField(
            model_name='structuredformate',
            name='UID',
        ),
        migrations.DeleteModel(
            name='JobDescription',
        ),
        migrations.DeleteModel(
            name='StructuredFormate',
        ),
    ]
