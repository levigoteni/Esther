# Generated by Django 2.2.6 on 2020-03-05 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='geek',
            name='photo',
            field=models.ImageField(default=2, upload_to='levi/media'),
            preserve_default=False,
        ),
    ]
