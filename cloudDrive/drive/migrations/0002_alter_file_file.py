# Generated by Django 5.1 on 2024-08-29 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=' '),
        ),
    ]
