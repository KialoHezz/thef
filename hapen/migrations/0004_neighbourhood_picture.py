# Generated by Django 4.0.2 on 2022-06-20 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hapen', '0003_user_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='hoodimages/'),
        ),
    ]
