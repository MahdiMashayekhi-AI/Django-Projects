# Generated by Django 4.2.2 on 2023-06-18 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/src/images/avatars'),
        ),
    ]