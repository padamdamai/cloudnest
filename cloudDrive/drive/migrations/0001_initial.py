# Generated by Django 4.2.14 on 2024-07-31 04:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folderName', models.CharField(default='Folder', max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('folderUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InnerFolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folderName', models.CharField(default='Folder', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parentFolder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drive.folder')),
            ],
        ),
        migrations.CreateModel(
            name='SubFolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folderName', models.CharField(default='Folder', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parentFolder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drive.innerfolder')),
            ],
        ),
        migrations.CreateModel(
            name='SubFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('fileUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drive.innerfolder')),
            ],
        ),
        migrations.CreateModel(
            name='InnerFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('fileUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drive.folder')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('fileUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
