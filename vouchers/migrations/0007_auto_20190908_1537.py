# Generated by Django 2.2.5 on 2019-09-08 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vouchers', '0006_auto_20190908_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voucher',
            name='discount_percent',
        ),
        migrations.AddField(
            model_name='voucher',
            name='discount_value_type',
            field=models.CharField(choices=[('Percent (%)', 'percent'), ('Number', 'number')], max_length=100, null=True),
        ),
    ]
