import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestSlowResources(unittest.TestCase):

    """SlowResources https://the-internet.herokuapp.com/slow"""

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "https://the-internet.herokuapp.com/slow"
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get(self.base_url)
        time.sleep(2)

    def test_something_is_on_the_page(self):
        driver = self.driver
        self.assertIn(self.base_url, driver.current_url)
        self.assertIn(driver.title, "The Internet")
        header = driver.find_element(By.CSS_SELECTOR, ".example > h3:nth-child(1)")
        self.assertTrue(header)
        print("Found header")
        time.sleep(2)
        main_text = driver.find_element(By.CSS_SELECTOR, ".example > p:nth-child(2)")
        self.assertTrue(main_text)
        print("Found main text")
        time.sleep(2)
        link_powered_by = driver.find_element(By.CSS_SELECTOR, ".large-4 > div:nth-child(2) > a:nth-child(1)")
        self.assertTrue(link_powered_by)
        print("Found link powered by")
        time.sleep(2)

        driver.save_screenshot("found_required_items.png")
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
