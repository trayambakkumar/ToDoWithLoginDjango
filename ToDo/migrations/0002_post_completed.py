# Generated by Django 3.0.4 on 2020-07-01 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
