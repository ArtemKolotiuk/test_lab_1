from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from pageobject.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, driver: WebDriver, page_id: str):
        super().__init__(driver)
        self.page_id = page_id

    def get_url(self) -> str:
        return f'{self.BaseUrl}/index.php?route=product/product&product_id= + {self.page_id}'

    def get_review_tab(self) -> WebElement:
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Reviews')

    def get_name_field(self) -> WebElement:
        return self.driver.find_element(By.ID, 'input-name')

    def get_review_field(self) -> WebElement:
        return self.driver.find_element(By.ID, 'input-review')

    def get_product_name(self) -> str:
        return self.driver.find_element(By.TAG_NAME, 'h1').text

    def get_brand_name(self) -> str:
        return self.driver.find_element(By.LINK_TEXT, 'Apple').text

    def get_product_code(self) -> str:
        return self.driver.find_element(By.XPATH, "//li[contains(text(),'Product Code: Product 15')]").text

    def get_product_price(self) -> str:
        return self.driver.find_element(By.XPATH, "//h2[contains(text(),'$110.00')]").text

    def get_product_description(self) -> str:
        return self.driver.find_element(By.XPATH, "//div[@id='tab-description']").text
