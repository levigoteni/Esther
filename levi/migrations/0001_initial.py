# Generated by Django 2.2.6 on 2020-03-05 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('prenom', models.CharField(max_length=25)),
                ('matricule', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
                ('niveau', models.CharField(max_length=25)),
                ('filiere', models.CharField(max_length=25)),
                ('AnneeA', models.CharField(max_length=25)),
            ],
        ),
    ]