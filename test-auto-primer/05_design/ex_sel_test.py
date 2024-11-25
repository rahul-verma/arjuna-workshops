# This file is a part of Arjuna-Workshops
# Copyright 2015-2021 Rahul Verma

# Website: www.RahulVerma.net

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from enum import Enum

# Singleton Config Class
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.app_url = "http://3.0.49.41/wp-admin"
            cls._instance.app_logout_url = "http://3.0.49.41/wp-login.php?action=logout"
            cls._instance.username = "user"
            cls._instance.password = "Okp!MuEfZ81P"
        return cls._instance

# Enum for browser selection
class BrowserType(Enum):
    CHROME = "chrome"
    FIREFOX = "firefox"

# Browser Factory Class
class Browser:
    def __init__(self, browser_type: BrowserType):
        self.driver = self._launch_browser(browser_type)
        self.waiter = WebDriverWait(self.driver, 30)

    @staticmethod
    def _launch_browser(browser_type: BrowserType):
        if browser_type == BrowserType.CHROME:
            options = ChromeOptions()
            driver_path = ChromeDriverManager().install()
            service = ChromeService(driver_path)
            return webdriver.Chrome(service=service, options=options)
        elif browser_type == BrowserType.FIREFOX:
            options = FirefoxOptions()
            driver_path = GeckoDriverManager().install()
            service = FirefoxService(driver_path)
            return webdriver.Firefox(service=service, options=options)
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")

    def quit(self):
        """Quit the browser."""
        self.driver.quit()

    def get(self, url):
        """Navigate to a URL."""
        self.driver.get(url)

    def find_element(self, locator_type, locator):
        """Wait and find an element."""
        return self.waiter.until(EC.presence_of_element_located((locator_type, locator)))

    def click_element(self, locator_type, locator):
        """Wait for and click an element."""
        element = self.waiter.until(EC.element_to_be_clickable((locator_type, locator)))
        element.click()

    def send_keys_to_element(self, locator_type, locator, keys):
        """Wait for an element and send keys."""
        element = self.waiter.until(EC.element_to_be_clickable((locator_type, locator)))
        element.send_keys(keys)

# Test Class
class SeleniumExampleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up test class")
        cls.config = Config()
        cls.browser = Browser(BrowserType.FIREFOX)

    @classmethod
    def tearDownClass(cls):
        print("Cleaning up test class")
        cls.browser.quit()

    def test_wp_login(self):
        """Test WordPress login functionality."""
        # Navigate to the login page
        self.browser.get(self.config.app_url)

        # Perform login actions
        self.browser.send_keys_to_element(By.NAME, "log", self.config.username)
        self.browser.send_keys_to_element(By.NAME, "pwd", self.config.password)
        self.browser.click_element(By.CSS_SELECTOR, "input[type*='sub']")

        # Assert successful login
        self.browser.find_element(By.XPATH, "//div[contains(*//text(), 'Welcome')]")

        # Log out
        self.browser.get(self.config.app_logout_url)


if __name__ == "__main__":
    unittest.main()
