# Generated by Django 4.1.1 on 2022-09-29 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_options_alter_razdel_options_work'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='description',
        ),
    ]
