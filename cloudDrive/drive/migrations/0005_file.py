# Generated by Django 4.2.14 on 2024-07-25 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0004_innerfolder'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(max_length=20)),
                ('file', models.FileField(upload_to='files')),
            ],
        ),
    ]
