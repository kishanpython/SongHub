# Generated by Django 2.0 on 2019-04-17 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0009_auto_20190416_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='file',
            field=models.FileField(default='', upload_to='musics/'),
            preserve_default=False,
        ),
    ]