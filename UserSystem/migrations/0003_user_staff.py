# Generated by Django 2.0.3 on 2018-03-06 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserSystem', '0002_auto_20180306_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]
