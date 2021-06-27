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
        self.driver.find_element_by_css_selector("[translate='CREATE_NEW_ACCOUNT']").click()
        self.driver.find_element_by_name("usernameRegisterPage").send_keys(username)
        self.driver.find_element_by_name("emailRegisterPage").send_keys(email)
        self.driver.find_element_by_name("passwordRegisterPage").send_keys(passw)
        self.driver.find_element_by_name("confirm_passwordRegisterPage").send_keys(repassw)
        self.driver.find_element_by_css_selector("[class = 'checkboxText roboto-light animated']").click()
        self.driver.find_element_by_id("register_btnundefined").click()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep


class init_Actions_AOS:
    """The class include actions from a first steps enter to the site and to register/login to account
                                    and until make a order"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def register(self, username: str, passw: str, repassw: str, email: str):
        """Register with new account, from order payment page, click register button and fills the account field"""
        self.driver.find_element_by_id("registration_btnundefined").click()
        self.driver.find_element_by_name("usernameRegisterPage").send_keys(username)
        self.driver.find_element_by_name("emailRegisterPage").send_keys(email)
        self.driver.find_element_by_name("passwordRegisterPage").send_keys(passw)
        self.driver.find_element_by_name("confirm_passwordRegisterPage").send_keys(repassw)
        self.driver.find_element_by_css_selector("[class = 'checkboxText roboto-light animated']").click()
        self.driver.find_element_by_id("register_btnundefined").click()

    def click_user_icon(self):
        self.driver.find_element_by_id("menuUser").click()

    def exit_window_user_icon(self):
        self.driver.find_element_by_class_name("closeBtn").click()

    def click_my_orders(self):
        self.driver.find_element_by_css_selector('a>div[class="mini-title"]>[class="option ng-scope"]').click()

    def my_orders(self):
       orders = self.driver.find_elements_by_css_selector('div>label[class="left ng-binding"]').text
       return orders

    def return_info_cart_products(self, number_of_products_in_cart):
        prices = self.driver.find_elements_by_xpath("//td[@class='smollCell']/p")
        quantities = self.driver.find_elements_by_css_selector("[class='smollCell quantityMobile']")
        names = self.driver.find_elements_by_class_name("roboto-regular productName ng-binding")

        list_products = []
        for i in range(number_of_products_in_cart):
            product = {names[i].text: f"price: {prices[i].text}, quantity: {quantities[i].text}"}
            list_products.append(product)
        return list_products

    def calculate_sum_price_of_cart(self, number_of_products_in_cart):
        prices = self.driver.find_elements_by_xpath("//td[@class='smollCell']/p")
        quantities = self.driver.find_elements_by_css_selector("[class='smollCell quantityMobile']")

        sum_cart = 0
        for i in range(number_of_products_in_cart):
            sum_cart += (int(prices[i].text)*int(quantities[i]))
        return sum_cart


    def sign_out_button(self):
        self.driver.find_element_by_css_selector('a>div>[translate="Sign_out"]').click()

    def click_next_button_shipdetails_page(self):
        """Click on next button in shipping details page"""
        next_button = self.driver.find_element_by_id('next_btn')
        self.driver.execute_script("arguments[0].click();", next_button)

    def choose_payment_method(self, payment_method: str, username: str, password: str):
        """insert a payment method(insert Small Caps) and fills the fields"""
        # version 2, check if the checkbox is selected
        self.driver.find_element_by_name(payment_method).click()
        self.driver.find_element_by_name("safepay_username").send_keys(username)
        self.driver.find_element_by_name("safepay_password").send_keys(password)
        self.driver.find_element_by_id("pay_now_btn_SAFEPAY").click()

    def order_number_in_thank_page(self):
        id_order = self.driver.find_element_by_id("orderNumberLabel").text
        return id_order

    def cart_page(self):
        self.driver.find_element_by_id("menuCart").click()

    def point_on_cart_icon(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_id("menuCart")).perform()

    def click_checkout_button(self):
        """click checkout button after point on cart icon"""
        self.driver.find_element_by_id("checkOutPopUp").click()

    def edit_product(self, num: str):
        edit = self.driver.find_element_by_css_selector('a[class="edit ng-scope"]')
        self.driver.execute_script("arguments[0].click();", edit)
        self.driver.find_element_by_name("quantity").click()
        self.driver.find_element_by_name("quantity").send_keys(num)
        self.driver.find_element_by_name("save_to_cart").click()
        init_Actions_AOS(self.driver).cart_page()

    def edit(self):
        for i in range(1,3):
            list1 = []
            list1.append(self.driver.find_elements_by_xpath(f'//tr[{i}]/td/span/a'))
            for edit in list1:
                sleep(5)
                edit.click()
                sleep(5)
                self.cart_page()



    def add_quantity(self, num: str):
        self.driver.find_element_by_name("quantity").click()
        self.driver.find_element_by_name("quantity").send_keys(num)
        self.driver.find_element_by_name("save_to_cart").click()

    def appear_quan_of_prod_in_cart(self):
        """return the quantity of the product As shown in the cart"""
        return self.driver.find_element_by_css_selector('[class="ng-scope"]>td>[class="ng-binding"]').text

    def total_quan_of_products_in_cart(self):
        """returns the total number of products in cart (each unit counts as a product)
        :return "x items"
        """
        return self.driver.find_element_by_xpath("//tfoot[@colspan='2']/tr/td/span/label").text

    def products_added_successfullt(self):
        self.driver.find_element_by_id





    def appear_text_thank_you_page(self):
        return self.driver.find_element_by_css_selector('[translate="Thank_you_for_buying_with_Advantage"]').text

    def appear_text_cart_empty(self):
        return self.driver.find_element_by_css_selector('[translate="Your_shopping_cart_is_empty"]').text

    def login(self, username: str, password: str):
        """Enter to account page and login to the account"""
        self.driver.find_element_by_id("menuUser").click()
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_id("sign_in_btnundefined").click()
        self.wait_homepage_loading()

    def back_to_homepage(self):
        """go back to home page from every screen"""
        self.driver.find_element_by_css_selector("a[translate='HOME']").click()

    def element_in_homepage(self):
        text = self.driver.find_element_by_id("headphonesTxt").text
        return text

    def back_to_category_page(self):
        """go back to home page from every screen"""
        self.driver.find_element_by_xpath(f'//nav[@class="pages fixedImportant productImage ng-scope"]/a[2]').click()

    def element_in_tablet_category_page(self):
        text = self.driver.find_element_by_class_name('categoryTitle').text
        return text

    def enter_category_from_homepage(self, Category_Name: str):
        """add a product to cart"""
        self.driver.find_element_by_id(f"{Category_Name}Img").click()

    def choose_product_from_current_category_page(self, Product_ID: str):
        self.driver.find_element_by_id(f"{Product_ID}").click()

    def choose_prod_color(self, Color_Name: str):
        self.driver.find_element_by_css_selector(f'[title="{Color_Name}"]')

    def wait_homepage_loading(self):
        """Wait for full loading of the home page"""
        self.wait.until(EC.visibility_of_element_located((By.ID, "headphonesTxt")))

    def wait_order_payment_page_loading(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3[translate="ORDER_PAYMENT"]')))

    def wait_payment_method_page_loading(self):
        self.wait.until(EC.visibility_of_element_located((By.NAME, "safepay_username")))

    def wait_account_icon_small_window_appear(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '["translate="Sign_out"]')))
