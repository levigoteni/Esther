# Generated by Django 2.2.6 on 2020-03-13 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levi', '0002_geek_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geek',
            name='photo',
        ),
    ]