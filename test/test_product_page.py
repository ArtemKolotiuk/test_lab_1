import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pageobject.product_page import ProductPage


class ProductPageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=self.options, service=Service(ChromeDriverManager().install()))
        self.product_page = ProductPage(self.driver, '42')
        self.product_page.open()
        self.product_price_expected: str = '$110.00'
        self.product_name: str = 'Apple Cinema 30"'
        self.product_brand_expected: str = 'Apple'
        self.product_code_expected: str = 'Product Code: Product 15'
        self.product_description: str = ("The 30-inch Apple Cinema HD Display delivers an amazing 2560 x 1600 pixel "
                                         "resolution")

    def tearDown(self) -> None:
        self.driver.close()

    def test_name(self):
        actual_name = self.product_page.get_product_name()
        self.assertEqual(self.product_name, actual_name)

    def test_brand(self):
        actual_brand = self.product_page.get_brand_name()
        self.assertEqual(self.product_brand_expected, actual_brand)

    def test_product_code(self):
        actual_code = self.product_page.get_product_code()
        self.assertEqual(self.product_code_expected, actual_code)

    def test_product_price(self):
        actual_price = self.product_page.get_product_price()
        self.assertEqual(self.product_price_expected, actual_price)

    def test_product_description(self):
        actual_description = self.product_page.get_product_description()
        self.assertIn(self.product_description, actual_description)
