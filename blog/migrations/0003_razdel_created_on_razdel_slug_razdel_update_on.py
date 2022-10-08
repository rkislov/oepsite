# Generated by Django 4.1.1 on 2022-09-27 09:11

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_razdel_alter_post_id_post_razdel'),
    ]

    operations = [
        migrations.AddField(
            model_name='razdel',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='razdel',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2022, 9, 27, 9, 11, 50, 395445, tzinfo=datetime.timezone.utc), max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='razdel',
            name='update_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
