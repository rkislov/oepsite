# Generated by Django 4.1.1 on 2022-09-27 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_parent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='parent_id',
            field=models.UUIDField(blank=True),
        ),
    ]
