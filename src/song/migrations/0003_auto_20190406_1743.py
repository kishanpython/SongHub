# Generated by Django 2.0 on 2019-04-06 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0002_try'),
    ]

    operations = [
        migrations.AlterField(
            model_name='try',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
