# Generated by Django 2.2.5 on 2019-09-06 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vouchers', '0004_auto_20190907_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voucher',
            name='id',
        ),
        migrations.AddField(
            model_name='voucher',
            name='discount_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]