# Generated by Django 4.2.5 on 2023-11-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_project_small_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='client',
            field=models.CharField(default='конкурс', max_length=50),
        ),
        migrations.AddField(
            model_name='project',
            name='full_space',
            field=models.CharField(default='конкурс', max_length=50),
        ),
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.CharField(default='конкурс', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='space',
            field=models.CharField(default='конкурс', max_length=50),
        ),
        migrations.AddField(
            model_name='project',
            name='years',
            field=models.CharField(default='конкурс', max_length=50),
        ),
    ]
