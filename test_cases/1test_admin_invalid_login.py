import time

import pytest
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_Page

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test01AdminLogin:
    admin_page_url = "https://profile.w3schools.com/login?redirect_url=https%3A%2F%2Fwww.w3schools.com%2F"

    username = "kbretchkin@gmail.com"
    password = "KBjobsearch1!"
    invalid_username = "adminrandom@yourstore.com"

         #  TC3: Testing InValid login
    def test_invalid_admin_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Sorry, looks like that’s the wrong email or password.')]"))
        )
        error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Sorry, looks like that’s the wrong email or password.')]").text

        time.sleep(2)

        print (error_message)
        print("success")
        if error_message == "Sorry, looks like that’s the wrong email or password.":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False








