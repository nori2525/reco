# Generated by Django 3.2.8 on 2021-11-19 12:15

from django.db import migrations, models
import reco.models


class Migration(migrations.Migration):

    dependencies = [
        ('reco', '0008_auto_20211112_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='single_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(storage=reco.models.OverwriteStorage(location='C:\\Users\\norimasa\\recom\\web\\mysite\\media'), upload_to='SImg', verbose_name='img')),
            ],
        ),
    ]
