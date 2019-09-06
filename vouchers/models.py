from django.db import models

# Create your models here.
class Voucher(models.Model):
    discount_id = models.AutoField(primary_key=True)
    discount_code = models.CharField(max_length=100, blank=False)
    discount_percent = models.DecimalField(max_digits=4,decimal_places=2,max_length=100,blank=False)
    max_use = models.BigIntegerField(blank=False, default=3)
    used = models.BigIntegerField(blank=False, default=0)

