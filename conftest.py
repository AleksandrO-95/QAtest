from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    try:
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
        driver.implicitly_wait(5)
        yield driver
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
        raise
    finally:
        driver.quit()