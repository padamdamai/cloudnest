# Generated by Django 4.2.14 on 2024-07-27 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0012_alter_innerfolder_folderuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='folderName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
