from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """Базовий клас"""
    BaseUrl: str

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.BaseUrl = 'http://54.183.112.233'

    def get_url(self) -> str:
        """Обовʼязково в дочірніх класах"""
        raise NotImplementedError

    def open(self) -> object:
        """Відкрити сторінку"""
        self.driver.get(self.get_url())
