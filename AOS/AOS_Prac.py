from selenium import webdriver
from AOS.Register_Login_out import init_reg_log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome(executable_path=r'C:\selenium\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://www.advantageonlineshopping.com/#/')
driver.maximize_window()
wait = WebDriverWait(driver, 20)
wait.until(EC.visibility_of_element_located((By.ID, "headphonesTxt"))).
# no user is active
try:
    driver.implicitly_wait(5)
    driver.find_element_by_id("menuUser").click()
    driver.find_element_by_css_selector('[translate="Sign_out"][href="javascript:void(0)"]').click()
except:
    driver.find_element_by_class_name('[class="closeBtn loginPopUpCloseBtn"]').click()
driver.implicitly_wait(10)

driver.find_element_by_class_name().send_keys()

