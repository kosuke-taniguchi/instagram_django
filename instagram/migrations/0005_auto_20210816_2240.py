# Generated by Django 3.2.5 on 2021-08-16 13:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_auto_20210816_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 16, 13, 40, 8, 344549, tzinfo=utc), null=True),
        ),
    ]