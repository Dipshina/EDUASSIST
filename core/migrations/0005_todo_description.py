# Generated by Django 3.1.6 on 2024-08-10 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_studymaterials_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, default='Enter your description here', null=True),
        ),
    ]
