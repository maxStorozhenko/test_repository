# Generated by Django 2.2.12 on 2020-05-22 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_logger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logger',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]