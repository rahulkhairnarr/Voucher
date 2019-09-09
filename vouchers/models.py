from django.db import models


# Create your models here.
class Voucher(models.Model):
    """ This model class store voucher code and its related information. It
    helps you to generate discount code with maximum usage
    """

    # DISCOUNT_VALUE_TYPE_CHOICE is create to make options available to select type of discount want to provide
    DISCOUNT_VALUE_TYPE_CHOICE = (
        ('percent', 'Percent (%)'),
        ('amount', 'Amount'),
    )

    # discount_id is automatically generate field and used as primary key to keep track of data
    discount_id = models.AutoField(primary_key=True)

    # discount_code takes unique code discount code combination of string and number
    discount_code = models.CharField(max_length=100, blank=False)

    # discount_value_type take type of discount you want to provide on specific code
    discount_value_type = models.CharField(max_length=100, blank=False,
                                           null=True, choices=DISCOUNT_VALUE_TYPE_CHOICE)

    # discount_value takes amount of discount want to provide on code
    discount_value = models.DecimalField(max_digits=4, decimal_places=2,
                                         max_length=100, blank=False,
                                         null=True, default=0)

    # max_voucher_use set maximum number of times speciic voucher code can use
    max_voucher_use = models.BigIntegerField(blank=False, default=3)

    # voucher_used keep track to numbers of time voucher code is used
    voucher_used = models.BigIntegerField(blank=False, default=0)
