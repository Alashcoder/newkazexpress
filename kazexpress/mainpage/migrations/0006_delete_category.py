# Generated by Django 3.2.8 on 2021-12-16 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_remove_product_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
