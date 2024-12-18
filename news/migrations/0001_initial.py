# Generated by Django 5.1.4 on 2024-12-14 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('base_url', models.URLField(unique=True)),
                ('scraping_pattern', models.TextField(help_text='CSS selectors for title and link in JSON format')),
            ],
        ),
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('image_url', models.URLField(blank=True, null=True)),
                ('video_url', models.URLField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('is_scraped', models.BooleanField(default=True)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='news.newssource')),
            ],
        ),
    ]
