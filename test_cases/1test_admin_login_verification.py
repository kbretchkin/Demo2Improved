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
    # admin_page_url = "https://www.w3schools.com/"
    # admin_page_urllogin = "https://profile.w3schools.com/login?redirect_url=https%3A%2F%2Fwww.w3schools.com%2F"
    username = "kbretchkin@gmail.com"
    password = "KBjobsearch1!"
    invalid_username = "adminrandom@yourstore.com"

    #  TC1
    def test_title_verification(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)

        # WebDriverWait(self.driver, 30)

        act_title = self.driver.title
        print(self.admin_page_url)
        print(self.driver.title)
        print("success")

        if act_title == "Log in - W3Schools":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False
