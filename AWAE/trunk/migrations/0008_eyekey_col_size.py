# Generated by Django 3.2 on 2021-07-27 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trunk', '0007_trunk_cols'),
    ]

    operations = [
        migrations.AddField(
            model_name='eyekey',
            name='col_size',
            field=models.IntegerField(default=1),
        ),
    ]
