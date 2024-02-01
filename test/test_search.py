import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageobject.search_page import SearchPage


class SearchPageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.name: str = 'apple'
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.search_page = SearchPage(self.driver)
        self.search_page.open()
        self.first_product_name: str = 'Apple'
        self.second_product_name: str = 'Sony'
        self.third_product_name: str = 'nokia'
        self.criteria_search_text: str = 'stunning'
        self.notification: str = 'There in no product that matches the search criteria.'
        self.firs_product_price: str = '$110.00'
        self.second_product_price: str = '$1202.00'


    def tearDown(self) -> None:
        self.driver.quit()

    def test_search(self):
        """Пошук продукту 'apple'"""
        self.search_page.search_by_name(self.first_product_name)
        self.assertEqual()
