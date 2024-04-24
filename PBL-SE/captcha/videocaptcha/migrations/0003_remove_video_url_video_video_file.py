# Generated by Django 5.0.3 on 2024-04-03 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videocaptcha', '0002_registereduser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='url',
        ),
        migrations.AddField(
            model_name='video',
            name='video_file',
            field=models.FileField(default='', upload_to='videos/'),
        ),
    ]