# Generated by Django 4.2.1 on 2023-05-23 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_post_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='post_default', null=True, upload_to='post_images/'),
        ),
    ]
