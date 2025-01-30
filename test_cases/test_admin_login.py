import time
import pytest
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_Page

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.read_properties import Read_Config
# Import utilities module with Log_Maker class
from utilities.custom_logger import Log_Maker

class Test01AdminLogin:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()

# Create logger object (for class at: utilities/custom_logger/Log_Maker)
# and call log_gen method
    logger = Log_Maker.log_gen()


    #  TC1
    def test_title_verification(self, setup):
        self.logger.info("************* Test01AdminLogin ****************")
        self.logger.info("************* verification of admin login page title ****************")
        self.driver = setup
        self.driver.get(self.admin_page_url)

        # WebDriverWait(self.driver, 30)

        act_title = self.driver.title
        exp_title = "Log in - W3Schools"
        print(self.admin_page_url)
        print(self.driver.title)
        print("success")


        if act_title == exp_title: #"Log in - W3Schools":
            self.logger.info("************* test_title_verification title matched ****************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("************* test_title_verification title not matched ****************")
            self.driver.close()
            assert False

         #  TC2: Testing Valid login
    def test_valid_admin_login(self, setup):
        self.logger.info("************* test_valid_admin_login started ****************")
        self.driver = setup
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
            self.logger.info("************* Dashboard text found ****************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.logger.info("************* Dashboard text not found ****************")
            self.driver.close()
            assert False

         #  TC3: Testing InValid login
    def test_invalid_admin_login(self, setup):
        self.logger.info("************* test_invalid_admin_login started ****************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Sorry, looks like that’s the wrong email or password.')]"))
        )
        error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Sorry, looks like that’s the wrong email or password.')]").text

        time.sleep(2)

        print (error_message)
        print("success")
        if error_message == "Sorry, looks like that’s the wrong email or password.":
            self.logger.info("************* test_invalid_admin_login error messages matched ****************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.logger.info("************* test_invalid_admin_login error messages not matched ****************")
            self.driver.close()
            assert False



