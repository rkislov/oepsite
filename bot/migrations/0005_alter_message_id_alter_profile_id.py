# Generated by Django 4.1.1 on 2022-10-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_alter_profile_external_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
