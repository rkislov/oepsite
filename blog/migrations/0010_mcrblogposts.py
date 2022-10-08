# Generated by Django 4.1.1 on 2022-09-29 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_post_razdel_post_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='McrBlogPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=2048)),
                ('desc', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
