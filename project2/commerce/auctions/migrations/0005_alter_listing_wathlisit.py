# Generated by Django 5.0.1 on 2024-01-18 06:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_listing_wathlisit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='wathlisit',
            field=models.ManyToManyField(related_name='listingWathlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
