# Generated by Django 4.1.4 on 2022-12-22 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_remove_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='social',
            field=models.JSONField(default='1', max_length=255),
            preserve_default=False,
        ),
    ]