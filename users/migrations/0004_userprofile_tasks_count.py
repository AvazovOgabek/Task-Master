# Generated by Django 5.0 on 2023-12-29 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='tasks_count',
            field=models.IntegerField(default=0),
        ),
    ]
