# Generated by Django 5.0.6 on 2024-07-04 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='introduce',
            field=models.FileField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='user_image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
