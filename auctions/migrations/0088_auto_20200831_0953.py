# Generated by Django 3.1 on 2020-08-31 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0087_auto_20200831_0822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
        migrations.AddField(
            model_name='comment',
            name='listing_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]