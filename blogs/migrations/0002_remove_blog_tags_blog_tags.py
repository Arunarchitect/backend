# Generated by Django 5.0.1 on 2024-01-28 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='tags',
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.CharField(default='BIM', max_length=20),
        ),
    ]
