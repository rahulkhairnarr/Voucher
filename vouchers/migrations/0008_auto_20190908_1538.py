# Generated by Django 2.2.5 on 2019-09-08 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vouchers', '0007_auto_20190908_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='discount_value_type',
            field=models.CharField(choices=[('percent', 'Percent (%)'), ('amount', 'Amount')], max_length=100, null=True),
        ),
    ]
