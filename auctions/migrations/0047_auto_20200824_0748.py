# Generated by Django 3.1 on 2020-08-24 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0046_listing_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='created_by',
            new_name='user',
        ),
    ]