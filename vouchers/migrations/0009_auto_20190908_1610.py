# Generated by Django 2.2.5 on 2019-09-08 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vouchers', '0008_auto_20190908_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voucher',
            old_name='max_use',
            new_name='max_voucher_use',
        ),
        migrations.RenameField(
            model_name='voucher',
            old_name='used',
            new_name='voucher_used',
        ),
    ]