# Generated by Django 2.2.1 on 2020-04-24 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200425_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.IntegerField(),
        ),
    ]
