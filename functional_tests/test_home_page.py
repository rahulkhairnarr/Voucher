from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from vouchers.models import Voucher
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time


class TestHomeDiscountCase(StaticLiveServerTestCase):
    """ This class check all html component and its function working properply using selenium"""

    # Setup function will run everytime when test start
    def setUp(self):
        # Initaited web driver with chrome path
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    # tearDown function will run everytime at end
    def tearDown(self):
        # At end of test close browser
        self.browser.close()

    # This function will check if card and content in page is load or not
    def test_product_card_load(self):
        # Providing url to browser
        self.browser.get(self.live_server_url)

        # this will find element with class name card
        alert = self.browser.find_element_by_class_name('card')

        # this will check if tag text in page is same or not
        self.assertEquals(
            alert.find_element_by_tag_name('span').text,
            'Burger'
        )

    # this function will check if apply code button click with entering code, it show validation error or not
    def test_click_on_button_without_code(self):
        # Providing url to browser
        self.browser.get(self.live_server_url)

        # finding button with class submit-code
        enter_code_btn = self.browser.find_element_by_id('submit-code')

        # after finding this method will click on button
        enter_code_btn.click()

        # this method will get all child selector inside button to verify if show validation popup
        pop_over = enter_code_btn.find_elements_by_css_selector("*")

        # if length is greater than 0 means it is showing validation error
        self.assertTrue(len(pop_over) > 0)

    # This method to check pop-up visible or not
    def test_click_on_button_with_code(self):
        # Providing url to browser
        self.browser.get(self.live_server_url)

        # this method will find input field to enter voucher code and enter code
        self.browser.find_element_by_name('discount_code').send_keys('RM 100')

        # this method will click on apply code by class name
        self.browser.find_element_by_id('submit-code').click()

        # pause for 2 seconds for popup to visible
        time.sleep(2)

        # if popup will visible then it will have title to verify
        self.assertEquals(self.browser.find_element_by_class_name('swal2-title').text, 'Oops...')
