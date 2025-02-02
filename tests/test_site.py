
import time
from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_s6(driver):

    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is('Samsung galaxy s6')
    time.sleep(5)

def test_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    time.sleep(3)
    homepage.click_monitors()
    time.sleep(3)
    homepage.check_product_count(2)
