# Generated by Django 3.2.5 on 2021-07-19 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BCSchain', '0004_auto_20210719_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='infblock',
            name='timestamp',
            field=models.IntegerField(default=None, verbose_name='Время блока'),
        ),
        migrations.AlterField(
            model_name='infblock',
            name='block_time',
            field=models.TimeField(verbose_name='Время старта блока'),
        ),
    ]