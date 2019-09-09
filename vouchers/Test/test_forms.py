from django.test import SimpleTestCase
from vouchers.forms import VoucherForm


class TestForms(SimpleTestCase):
    """ This class will check, if empty data is pass in form it throw error or not"""

    def test_discount_field(self):
        form = VoucherForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
