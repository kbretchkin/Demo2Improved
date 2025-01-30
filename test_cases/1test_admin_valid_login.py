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

         #  TC2: Testing Valid login
    def test_valid_admin_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[@class='learntocodeh1']"))
        )

        act_dashboard_text = self.driver.find_element(By.XPATH,"//h1[@class='learntocodeh1']").text
        print(act_dashboard_text)
        print("successfully logged in and validated text")

        if act_dashboard_text == "Learn to Code":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

