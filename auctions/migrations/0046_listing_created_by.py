# Generated by Django 3.1 on 2020-08-24 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0045_remove_listing_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auctions.user'),
            preserve_default=False,
        ),
    ]
