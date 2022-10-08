# Generated by Django 4.1.1 on 2022-09-30 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_delete_mcrblogposts'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentBlogPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=2048)),
                ('desc', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
