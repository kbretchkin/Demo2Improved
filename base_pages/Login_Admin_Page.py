import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class Login_Admin_Page:
    # define locators
    textbox_username = 'email'
    textbox_password = 'password'
    btn_login_xpath = "// button[ @ type = 'submit']"


    # creating constructor
    def __init__(self,driver):
        self.driver = driver

    # writing 3 action methods
    # action 1 username
    def enter_username(self,email):
        self.driver.find_element(By.NAME,self.textbox_username).clear()
        self.driver.find_element(By.NAME,self.textbox_username).send_keys(email)

    # action 2 password
    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.textbox_password).clear()
        self.driver.find_element(By.NAME, self.textbox_password).send_keys(password)

        # action 3 submit
    def click_login(self):
            self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

