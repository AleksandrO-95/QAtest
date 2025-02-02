from selenium.webdriver.common.by import By
from conftest import driver

class HomePage:
    def __init__(self, driver):
        self.driver = driver
    def open(self):
        self.driver.get('https://www.demoblaze.com/index.html')

    def click_galaxy_s6(self):
        galaxy_s6 = self.driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
        # кликаем
        galaxy_s6.click()

    def click_monitors(self):
        monitors = self.driver.find_element(By.XPATH, "//a[text()='Monitors']")
        monitors.click()

    def check_product_count(self, count):
        div_monitors = self.driver.find_elements(By.CSS_SELECTOR, '.card')
        assert len(div_monitors) == count
