# Generated by Django 4.2.4 on 2023-08-29 14:48

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='editor_news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=225)),
                ('news_desc', tinymce.models.HTMLField()),
            ],
        ),
    ]
