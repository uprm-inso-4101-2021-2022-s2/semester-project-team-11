# Generated by Django 4.0.3 on 2022-04-07 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeservice', '0007_remove_clientaccount_user_name_remove_job_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ('-time',)},
        ),
        migrations.RenameField(
            model_name='job',
            old_name='posted',
            new_name='time',
        ),
    ]
