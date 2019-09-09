from django.test import SimpleTestCase
from django.urls import reverse, resolve
from vouchers.views import home_view


class TestUrls(SimpleTestCase):
    """ This class check url and output page """

    def test_home_url_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home_view)