# Generated by Django 4.0.2 on 2022-03-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='static/user/images/default_profile.jpg', null=True, upload_to='profile_images'),
        ),
    ]
