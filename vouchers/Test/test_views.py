from django.test import TestCase, Client
from django.urls import reverse
from vouchers.models import Voucher


class TestViews(TestCase):
    """This class check Views.py funtion are working or not"""

    # Setup Intitaling classes instance
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.voucher1 = Voucher.objects.create(
            discount_code='RM 10',
            discount_value_type='amount',
            discount_value=10.00,
            max_voucher_use=3,
            voucher_used=0
        )

    # Function to check home_view get condition working or not
    def test_home_view_GET(self):

        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    # Function to check home_view post condition working or not
    def test_home_view_POST(self):

        response = self.client.post(self.home_url, {
            'discount_code': 'RM 10'
        })
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.voucher1.discount_value, 10.00)