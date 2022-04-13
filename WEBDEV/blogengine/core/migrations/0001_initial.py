# Generated by Django 4.0.3 on 2022-03-16 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=128)),
                ('slug', models.SlugField(max_length=128)),
                ('body', models.TextField(blank=True, db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
