# Generated by Django 3.2.9 on 2021-12-09 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_auto_20211209_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
