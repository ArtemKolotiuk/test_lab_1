from dataclasses import dataclass
from decimal import Decimal
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pageobject.base_page import BasePage


def extract_decimal_price(text: str) -> Decimal:
    """Функция, которая извлекает из строки цену"""

    # text == "$110.00 $122.00\nEx Tax: $90.00"
    split_by_lines: List[str] = text.split("\n")
    # split_by_lines == ["$110.00 $122.00", "Ex Tax: $90.00"]

    first_price_lines = split_by_lines[0].split(' ')
    # first_price == ["$110.00", "$122.00"]

    # Удаляем первый символ (доллар)
    first_price = first_price_lines[0][1:]
    # В случае 1,202.00 нужно убрать запятую.
    first_price_without_punctuation = first_price.replace(",", "")

    return Decimal(first_price_without_punctuation)
@dataclass
class ProductInfo:
    name: str
    price: Decimal
class SearchPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_url(self) -> str:
        return f'{self.BaseUrl}/index.php?route=product/search'

    def get_search_field(self)->WebElement:
        return self.driver.find_element(By.NAME, 'search')

    def get_search_criteria_field(self)->WebElement:
        return self.driver.find_element(By.ID, 'input-search')

    def get_btn_search_criteria(self)->WebElement:
        return self.driver.find_element(By.ID, 'button-search')

    def get_btn_search(self)-> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, '#button-search')


    def clear_search_field(self):
        self.get_search_field().clear()

    def clear_search_criteria_field(self):
        self.get_search_criteria_field().clear()

    def input_search(self):
        pass

    def get_product_name(self) -> str:
        return self.driver.find_element(By.TAG_NAME, 'h4').text

    def get_product_price(self) -> str:
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'$110.00')]").text

    def search_by_name(self, name: str):
        self.get_search_field().send_keys(name)
        self.get_btn_search().click()

    def get_search_results(self) -> List[ProductInfo]:
        products_tags = self.driver.find_elements(By.CLASS_NAME, 'product-layout')
        products: List[ProductInfo] = []
        for product_div_tag in products_tags:
            name: str = product_div_tag.find_element(By.TAG_NAME, 'h4').text
            price_text: str = product_div_tag.find_element(By.CLASS_NAME, 'price').text
            product = ProductInfo(name=name, price=Decimal(extract_decimal_price(price_text)))
            products.append(product)
            return products

