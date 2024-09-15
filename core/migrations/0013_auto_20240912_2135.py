# Generated by Django 3.1.6 on 2024-09-12 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0012_remove_studymaterials_user_alter_category_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('IT', 'IT'), ('Business Management', 'Business Management'), ('Hotel Management', 'Hotel Management'), ('Finance', 'Finance'), ('Arts', 'Arts')], max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='study_materials/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.topic')),
            ],
        ),
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RemoveField(
            model_name='studymaterials',
            name='category',
        ),
        migrations.RemoveField(
            model_name='studymaterials',
            name='description',
        ),
        migrations.AddField(
            model_name='studymaterials',
            name='subject',
            field=models.CharField(choices=[('IT', 'IT'), ('Business Management', 'Business Management'), ('Hotel Management', 'Hotel Management'), ('Finance', 'Finance'), ('Arts', 'Arts')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studymaterials',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='study_materials', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='studymaterials',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='studymaterials',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='topic',
            name='materials',
            field=models.ManyToManyField(blank=True, to='core.StudyMaterials'),
        ),
    ]
