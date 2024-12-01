# Generated by Django 4.2.16 on 2024-12-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/products'),
        ),
        migrations.AddField(
            model_name='shop',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/shops'),
        ),
    ]