# Generated by Django 4.2.2 on 2024-09-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20240912_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
