# Generated by Django 4.0.3 on 2022-04-03 00:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(null=True)),
                ('specialty', models.CharField(max_length=128)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('incomplete', 'Incomplete'), ('fulfilled', 'Fulfilled')], default='incomplete', max_length=10)),
                ('slug', models.SlugField(max_length=250, unique_for_date='posted')),
                ('posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-posted',),
            },
        ),
    ]