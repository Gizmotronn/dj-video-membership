# Generated by Django 3.0.9 on 2020-08-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_video_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
