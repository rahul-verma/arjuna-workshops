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
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SeleniumExampleTest(unittest.TestCase):

    def setUp(self):
        print("Setting up")
        self.__app_url = "http://3.0.49.41/wp-admin"
        self.__app_logout_url = "http://3.0.49.41/wp-login.php?action=logout"
        self.username = "user"
        self.password = "Okp!MuEfZ81P"
        
        # Setup Chrome options
        #options = ChromeOptions()
        #driver_path = ChromeDriverManager().install()
        #self.svc = ChromeService(driver_path)
        options = FirefoxOptions()
        driver_path = GeckoDriverManager().install()
        self.svc = FirefoxService(driver_path)
        
        self.svc.start()
        self.driver = webdriver.Remote(self.svc.service_url, options=options)
        self.waiter = WebDriverWait(self.driver,30)

    def tearDown(self):
        print("Cleaning up")
        self.driver.quit()
        self.svc.stop()

    def test_wp_login(self):
        self.driver.get(self.__app_url)
        self.waiter.until(EC.presence_of_element_located((By.ID, "wp-submit")))
        element = self.waiter.until(EC.element_to_be_clickable((By.NAME, "log")))
        element.send_keys(self.username)
        element = self.waiter.until(EC.element_to_be_clickable((By.NAME, "pwd")))
        element.send_keys(self.password)
        element = self.waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type *= 'sub']")))
        element.click()
        self.waiter.until(EC.presence_of_element_located((By.XPATH, "//div[contains(*//text(), 'Welcome')]")))
        self.driver.get(self.__app_logout_url)

unittest.main()
