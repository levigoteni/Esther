# Generated by Django 2.2.6 on 2020-03-23 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levi', '0003_remove_geek_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='geek',
            name='photo',
            field=models.ImageField(default=9, upload_to='levi/media'),
            preserve_default=False,
        ),
    ]
