# Generated by Django 2.2.5 on 2019-09-06 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vouchers', '0003_auto_20190907_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='max_use',
            field=models.BigIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='used',
            field=models.BigIntegerField(default=0),
        ),
    ]