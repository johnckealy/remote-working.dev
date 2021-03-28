# Generated by Django 3.1.7 on 2021-03-28 18:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ignore_tag_chips',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=300, null=True), default=list, size=60),
        ),
    ]
