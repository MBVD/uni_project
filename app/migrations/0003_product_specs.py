# Generated by Django 4.2.17 on 2024-12-08 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specs',
            field=models.JSONField(null=True),
        ),
    ]
