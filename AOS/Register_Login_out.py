from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class init_reg_log:
    """The class for the first steps enter to the site and to register/login to account"""
    def __init__(self, driver):
        self.driver = driver

    def register(self, username, passw, repassw, email):
        self.driver.find_element_by_id("menuUser").click()
        self.driver.find_element_by_class_name("create-new-account ng-scope").click()
        self.driver.find_element_by_class_name("usernameRegisterPage").send_keys(username)
        self.driver.find_element_by_class_name("emailRegisterPage").send_keys(email)
        self.driver.find_element_by_class_name("passwordRegisterPage").send_keys(passw)
        self.driver.find_element_by_class_name("confirm_passwordRegisterPage").send_keys(repassw)
        self.driver.find_element_by_class_name("checkboxText roboto-light animated").click()




