# Generated by Django 4.2.5 on 2023-11-15 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_remove_projectsphoto_is_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='main_photo',
        ),
    ]
