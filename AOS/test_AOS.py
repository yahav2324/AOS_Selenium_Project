from unittest import TestCase
from selenium import webdriver
from AOS.AOS_POM import init_Actions_AOS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from time import sleep
class test_AOS(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\selenium\chromedriver.exe')
        self.driver.implicitly_wait(20)
        self.driver.get('https://www.advantageonlineshopping.com/#/')
        self.driver.maximize_window()
        # no user is active
        init_Actions_AOS(self.driver).login('lol1234', 'Lol1234')
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.ID, "headphonesTxt")))

    def tearDown(self):
        self.driver.close()

    def test_chang_quan_and_update_in_cart(self):
        """The quantity of the product will be change and the quantity of the product
         in the cart page will be Changed accordingly"""
        # choose a product 1
        init_Actions_AOS(self.driver).enter_category_from_homepage('speakers')
        init_Actions_AOS(self.driver).choose_product_from_current_category_page('25')
        init_Actions_AOS(self.driver).choose_prod_color('BLACK')
        init_Actions_AOS(self.driver).add_quantity("3")
        # return home page by navigation bar
        init_Actions_AOS(self.driver).back_to_homepage()
        # waiting for loading home page
        init_Actions_AOS(self.driver).wait_homepage_loading()
        # choose a product 2
        init_Actions_AOS(self.driver).enter_category_from_homepage('tablets')
        init_Actions_AOS(self.driver).choose_product_from_current_category_page('17')
        init_Actions_AOS(self.driver).choose_prod_color('GRAY')
        init_Actions_AOS(self.driver).add_quantity("5")
        # Enter to cart page
        init_Actions_AOS(self.driver).cart_page()
        # edit product 1
        init_Actions_AOS(self.driver).edit_product('4')
        # check after the product changed, if the cart will be changed accordingly
        self.assertEqual('4', init_Actions_AOS(self.driver).appear_quan_of_prod_in_cart())


    def test_return_back(self):
        # choose a product 1
        init_Actions_AOS(self.driver).enter_category_from_homepage('tablets')
        init_Actions_AOS(self.driver).choose_product_from_current_category_page('18')
        init_Actions_AOS(self.driver).choose_prod_color('GRAY')
        init_Actions_AOS(self.driver).add_quantity("5")
        # return category page by navigation bar
        init_Actions_AOS(self.driver).back_to_category_page()
        # check if the current page is tablet category
        text_tablets = init_Actions_AOS(self.driver).element_in_tablet_category_page()
        self.assertEqual('TABLETS', text_tablets)
        init_Actions_AOS(self.driver).back_to_homepage()
        text_in_HomeP = init_Actions_AOS(self.driver).element_in_homepage()
        self.assertEqual('HEADPHONES', text_in_HomeP)

    def test_full_order_actions(self):
        init_Actions_AOS(self.driver).click_user_icon()
        init_Actions_AOS(self.driver).sign_out_button()
        init_Actions_AOS(self.driver).wait_homepage_loading()
        init_Actions_AOS(self.driver).enter_category_from_homepage('mice')
        init_Actions_AOS(self.driver).choose_product_from_current_category_page('27')
        init_Actions_AOS(self.driver).choose_prod_color('PURPLE')
        init_Actions_AOS(self.driver).add_quantity('3')
        init_Actions_AOS(self.driver).point_on_cart_icon()
        init_Actions_AOS(self.driver).click_checkout_button()
        init_Actions_AOS(self.driver).wait_order_payment_page_loading()
        init_Actions_AOS(self.driver).register('lol41', 'Lol31', 'Lol31', 'lol41@gmail.com')
        init_Actions_AOS(self.driver).wait_order_payment_page_loading()
        init_Actions_AOS(self.driver).click_next_button_shipdetails_page()
        init_Actions_AOS(self.driver).wait_payment_method_page_loading()
        init_Actions_AOS(self.driver).choose_payment_method('safepay', 'ya11', 'Ya11')
        successfully_order = init_Actions_AOS(self.driver).appear_text_thank_you_page()
        self.assertEqual('Thank you for buying with Advantage', successfully_order)
        id_order = init_Actions_AOS(self.driver).order_number_in_thank_page()
        init_Actions_AOS(self.driver).cart_page()
        empty_cart = init_Actions_AOS(self.driver).appear_text_cart_empty()
        self.assertEqual('Your shopping cart is empty', empty_cart)
        init_Actions_AOS(self.driver).click_user_icon()
        init_Actions_AOS(self.driver).click_my_orders()
        all_orders = init_Actions_AOS(self.driver).my_orders()
        self.assertIn(id_order, all_orders)














