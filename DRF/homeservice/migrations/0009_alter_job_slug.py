# Generated by Django 4.0.3 on 2022-04-07 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeservice', '0008_alter_job_options_rename_posted_job_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='time'),
        ),
    ]