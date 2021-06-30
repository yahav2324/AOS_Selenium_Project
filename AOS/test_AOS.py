from unittest import TestCase
from selenium import webdriver
from AOS.AOS_POM import init_Actions_AOS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import locale
from time import sleep
from AOS.EXCEL import *

class TestAOS(TestCase):

    def setUp(self):
        """
        setUp function, open and initial the environment and "settings" for the tests
        """
        # self.driver = webdriver.Chrome(executable_path=r'C:\selenium\chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\itama\Desktop\selenium\chromedriver.exe')
        self.driver.implicitly_wait(15)
        self.driver.get('https://www.advantageonlineshopping.com/#/')
        self.driver.maximize_window()
        self.driver.refresh()
        self.wait = WebDriverWait(self.driver, 20)
        self.wait.until(EC.visibility_of_element_located((By.ID, "headphonesTxt")))

    def tearDown(self):
        """ closing the website at the end of each test"""
        self.driver.close()

    def test1(self):

        # add first product
        test1 = init_Actions_AOS(self.driver)
        test1.enter_category_from_homepage(data(0, 0))
        test1.choose_product_from_current_category_page(data(0, 1))
        test1.choose_prod_color(data(0, 3))
        test1.add_quantity_and_click_add(data(0, 2))

        # add second product
        test1.click_back()
        test1.choose_product_from_current_category_page(data(0, 4))
        test1.choose_prod_color(data(0, 6))
        test1.add_quantity_and_click_add(data(0, 5))

        # check that cart icon appears with the right amount of products (quantity greater then 1 counts x products)
        self.assertIn(f"{int(data(0, 2))+int(data(0, 5))} Items", test1.total_quan_of_products_in_cart())

    def test2(self):

        # add first product
        test2 = init_Actions_AOS(self.driver)
        test2.enter_category_from_homepage(data(1, 0))
        test2.choose_product_from_current_category_page(data(1, 1))
        name1 = self.driver.find_element_by_css_selector("h1[class='roboto-regular ng-binding']").text
        price1 = self.driver.find_element_by_css_selector('h2[class="roboto-thin screen768 ng-binding"]').text
        test2.choose_prod_color(data(1, 3))
        test2.add_quantity_and_click_add(data(1, 2))

        # add second product
        test2.click_back()
        test2.choose_product_from_current_category_page(data(1, 4))
        name2 = self.driver.find_element_by_css_selector("h1[class='roboto-regular ng-binding']").text
        price2 = self.driver.find_element_by_css_selector('h2[class="roboto-thin screen768 ng-binding"]').text
        test2.choose_prod_color(data(1, 6))  # new
        test2.add_quantity_and_click_add(data(1, 5))

        # add third product
        test2 = init_Actions_AOS(self.driver)
        test2.back_to_homepage()
        test2.enter_category_from_homepage(data(1, 7))
        test2.choose_product_from_current_category_page(data(1, 8))
        name3 = self.driver.find_element_by_css_selector("h1[class='roboto-regular ng-binding']").text
        price3 = self.driver.find_element_by_css_selector('h2[class="roboto-thin screen768 ng-binding"]').text
        test2.choose_prod_color(data(1, 10))
        test2.add_quantity_and_click_add(data(1, 9))

        # collecting all the date necessary from the cart icon
        names = self.driver.find_elements_by_css_selector("h3[class='ng-binding']")
        quantities = self.driver.find_elements_by_xpath("//a/label[@class = 'ng-binding'][1]")
        colors = self.driver.find_elements_by_css_selector("span[class='ng-binding']")
        prices = self.driver.find_elements_by_css_selector('[class="price roboto-regular ng-binding"]')

        # setting the products info, according to the cart icon info
        product3 = \
            f"{names[0].text}: quantity is {quantities[0].text}, color is {colors[0].text}, price is {prices[0].text} "
        product2 = \
            f"{names[1].text}: quantity is {quantities[1].text}, color is {colors[1].text}, price is {prices[1].text} "
        product1 = \
            f"{names[2].text}: quantity is {quantities[2].text}, color is {colors[2].text}, price is {prices[2].text} "

        # each product price according to information that was collected from the product page, and the excel data file
        total_money_for_product_1 = \
             test2.convert_numbers_to_money_form(test2.convers_money_to_number(price1) * int(data(1, 2)))
        total_money_for_product_2 = \
             test2.convert_numbers_to_money_form(test2.convers_money_to_number(price2) * int(data(1, 5)))
        total_money_for_product_3 = \
             test2.convert_numbers_to_money_form(test2.convers_money_to_number(price3) * int(data(1, 9)))

        # test product 1
        print(data(1, 3))
        self.assertIn(name1[:25], product1)
        self.assertIn(str(data(1, 2)), product1)
        self.assertIn(data(1, 3), product1)
        self.assertIn(total_money_for_product_1, prices[2].text)
        # test product 2
        self.assertIn(name2[:25], product2)
        self.assertIn(str(data(1, 5)), product2)
        self.assertIn(data(1, 6), product2)
        self.assertIn(total_money_for_product_2, prices[1].text)
        # test product 3
        self.assertIn(name3[:25], product3)
        self.assertIn(str(data(1, 9)), product3)
        self.assertIn(data(1, 10), product3)
        self.assertIn(total_money_for_product_3, prices[0].text)



    def test3(self):
        # add a product
        test3 = init_Actions_AOS(self.driver)
        test3.enter_category_from_homepage(data(2, 0))
        test3.choose_product_from_current_category_page(data(2, 1))
        product1 = self.driver.find_element_by_css_selector('h1[class="roboto-regular screen768 ng-binding"]').text
        test3.choose_prod_color(data(2, 3))
        test3.add_quantity_and_click_add(data(2, 2))

        # add second product
        test3.click_back()
        test3.choose_product_from_current_category_page(data(2, 4))
        product2 = self.driver.find_element_by_css_selector('h1[class="roboto-regular screen768 ng-binding"]').text
        test3.choose_prod_color(data(2, 6))
        test3.add_quantity_and_click_add(data(2, 5))

        # remove the last product added
        test3.point_on_cart_icon() # new
        self.driver.find_element_by_xpath('//ul/li/tool-tip-cart/div/table/tbody/tr[1]/td/div/' 
                                                  'div[@class="removeProduct iconCss iconX"]').click()

        # check that only the first product is left in cart
        self.assertNotIn(product2[0:25], self.driver.find_element_by_css_selector("h3[class='ng-binding']").text)
        self.assertIn(product1[0:25], self.driver.find_element_by_css_selector("h3[class='ng-binding']").text)

    def test4(self):

        test4 = init_Actions_AOS(self.driver)

        # add a product
        test4.enter_category_from_homepage(data(3, 0))
        test4.choose_product_from_current_category_page(data(3, 1))
        test4.choose_prod_color(data(3, 3))
        test4.add_quantity_and_click_add(data(3, 2))
        test4.cart_page()
        self.assertEqual(self.driver.find_element_by_css_selector("[class='select  ng-binding']").text, "SHOPPING CART")

    def test5(self):
        # add a product with quantity = 3
        test5 = init_Actions_AOS(self.driver)
        test5.enter_category_from_homepage(data(4, 0))
        test5.choose_product_from_current_category_page(data(4, 1))
        price1 = test5.calculate_product_price_with_quantity(data(4, 2))
        test5.choose_prod_color(data(4, 3))

        test5.add_quantity_and_click_add(data(4, 2))

        # add second product
        test5.click_back()
        test5.choose_product_from_current_category_page(data(4, 4))
        price2 = test5.calculate_product_price_with_quantity(data(4, 5))
        test5.choose_prod_color(data(4, 6))
        test5.add_quantity_and_click_add(data(4, 5))


        # add third product
        test5 = init_Actions_AOS(self.driver)
        test5.back_to_homepage()
        test5.enter_category_from_homepage(data(4, 7))
        test5.choose_product_from_current_category_page(data(4, 8))
        price3 = test5.calculate_product_price_with_quantity(data(4, 9))
        test5.choose_prod_color(data(4, 10))
        test5.add_quantity_and_click_add(data(4, 9))

        # move to cart page
        test5.cart_page()

        # converting the prices to a final price in money format
        sum_prices = price1+price2+price3
        sum_prices = test5.convert_numbers_to_money_form(sum_prices)

        # summing the prices of the products
        self.assertIn(sum_prices, self.driver.find_element_by_css_selector(
            "#shoppingCart > table > tfoot > tr:nth-child(1) > td:nth-child(2) > span.roboto-medium.ng-binding").text)

        # printing all cart products info
        print("The products in cart: ")
        for product in test5.return_info_cart_products(3):
            print(product)

    def test6(self):
        """The quantity of the product will be change and the quantity of the product
         in the cart page will be Changed accordingly"""
        # add a products
        init_Actions_AOS(self.driver).enter_category_from_homepage(data(5, 0))
        init_Actions_AOS(self.driver).choose_product_from_current_category_page(data(4, 1))
        init_Actions_AOS(self.driver).choose_prod_color(data(5, 3))
        init_Actions_AOS(self.driver).add_quantity_and_click_add(data(5, 2))
        # return home page by navigation bar
        init_Actions_AOS(self.driver).back_to_homepage()
        # waiting for loading home page
        init_Actions_AOS(self.driver).wait_homepage_loading()
        # add second product
        init_Actions_AOS(self.driver).enter_category_from_homepage(data(5, 4))
        init_Actions_AOS(self.driver).choose_product_from_current_category_page(data(5, 5))
        init_Actions_AOS(self.driver).choose_prod_color(data(5, 7))
        init_Actions_AOS(self.driver).add_quantity_and_click_add(data(5, 6))
        # Enter to cart page
        init_Actions_AOS(self.driver).cart_page()
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, '//li/tool-tip-cart/div/table/tfoot/tr/td/button')))
        # edit all products
        init_Actions_AOS(self.driver).edit_products(2)
        # check that cart got changed accordingly to the edits that been made
        products = init_Actions_AOS(self.driver).return_quantity_cart_products(2)
        print(f"products: {products}")
        self.assertIn('6', products[0])
        self.assertIn('7', products[1])


    def test7(self):
        # choose a product
        init_Actions_AOS(self.driver).enter_category_from_homepage(data(6, 0))
        init_Actions_AOS(self.driver).choose_product_from_current_category_page(data(6, 1))
        print(data(6, 3))
        init_Actions_AOS(self.driver).choose_prod_color(data(6, 3))
        # init_Actions_AOS(self.driver).choose_prod_color("BLUE")
        init_Actions_AOS(self.driver).add_quantity_and_click_add(data(6, 2))

        # return category page by navigation bar
        init_Actions_AOS(self.driver).click_back()

        # check if the current page is a tablet category
        text_tablets = init_Actions_AOS(self.driver).element_in_tablet_category_page()
        self.assertEqual('TABLETS', text_tablets)

        # check if the current page is a homepage
        init_Actions_AOS(self.driver).click_back()
        text_in_homep = init_Actions_AOS(self.driver).element_in_homepage()
        self.assertEqual('HEADPHONES', text_in_homep)

    def test8(self):
        init_Actions_AOS(self.driver).enter_category_from_homepage(data(7, 0))
        init_Actions_AOS(self.driver).choose_product_from_current_category_page(data(7, 1))
        init_Actions_AOS(self.driver).choose_prod_color(data(7, 3))
        init_Actions_AOS(self.driver).add_quantity_and_click_add(data(7, 2))
        init_Actions_AOS(self.driver).point_on_cart_icon()
        init_Actions_AOS(self.driver).click_checkout_button()
        init_Actions_AOS(self.driver).wait_order_payment_page_loading()
        init_Actions_AOS(self.driver).register(data(7, 4), data(7, 6), data(7, 6), data(7, 5))  # new
        init_Actions_AOS(self.driver).wait_order_payment_page_loading()
        init_Actions_AOS(self.driver).click_next_button_shipdetails_page()
        init_Actions_AOS(self.driver).wait_payment_method_page_loading()
        init_Actions_AOS(self.driver).choose_safepay_payment_method(data(7, 7), data(7, 8))  # new
        init_Actions_AOS(self.driver).wait_thank_page_appear()  # new
        successfully_order = init_Actions_AOS(self.driver).appear_text_thank_you_page()
        self.assertEqual('Thank you for buying with Advantage', successfully_order)
        id_order = init_Actions_AOS(self.driver).order_number_in_thank_page()
        init_Actions_AOS(self.driver).cart_page()
        init_Actions_AOS(self.driver).wait_cart_page_appear()  # new
        empty_cart = init_Actions_AOS(self.driver).appear_text_cart_empty()
        self.assertEqual('Your shopping cart is empty', empty_cart)
        init_Actions_AOS(self.driver).click_user_icon()
        init_Actions_AOS(self.driver).click_my_orders()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3[translate="MY_ORDERS"]')))
        all_orders = init_Actions_AOS(self.driver).my_orders()
        print(all_orders)
        self.assertIn(id_order, all_orders)

    def test9(self):
        init_Actions_AOS(self.driver).enter_category_from_homepage(data(8, 0))
        init_Actions_AOS(self.driver).choose_product_from_current_category_page(data(8, 1))
        init_Actions_AOS(self.driver).choose_prod_color(data(8, 3))
        init_Actions_AOS(self.driver).add_quantity_and_click_add(data(8, 2))

        init_Actions_AOS(self.driver).point_on_cart_icon()
        init_Actions_AOS(self.driver).click_checkout_button()
        init_Actions_AOS(self.driver).wait_order_payment_page_loading()

        init_Actions_AOS(self.driver).login_from_order_payment_page(data(8, 4), data(8, 5))
        init_Actions_AOS(self.driver).wait_order_payment_page_loading()
        init_Actions_AOS(self.driver).click_next_button_shipdetails_page()
        init_Actions_AOS(self.driver).wait_order_payment_page_loading()
        # init_Actions_AOS(self.driver).choose_safepay_payment_method('ya112', 'Ya11')
        init_Actions_AOS(self.driver).choose_mastercredit_payment_method(data(8, 6),
                                                                         data(8, 7), data(8, 8), data(8, 9), data(8, 10))
        init_Actions_AOS(self.driver).wait_thank_page_appear()
        id_order = init_Actions_AOS(self.driver).order_number_in_thank_page()

        init_Actions_AOS(self.driver).cart_page()
        init_Actions_AOS(self.driver).wait_cart_page_appear()
        empty_cart = init_Actions_AOS(self.driver).appear_text_cart_empty()
        self.assertEqual('Your shopping cart is empty', empty_cart)

        init_Actions_AOS(self.driver).click_user_icon()
        init_Actions_AOS(self.driver).click_my_orders()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="left ng-scope"]')))
        all_orders = init_Actions_AOS(self.driver).my_orders()
        self.assertIn(id_order, all_orders)

    def test10(self):
        test10 = init_Actions_AOS(self.driver)
        test10.login(data(9, 0), data(9, 1))
        self.wait.until(EC.invisibility_of_element_located((By.ID, 'sign_in_btnundefined')))
        test10.click_user_icon()
        try:
            self.driver.find_element_by_css_selector("[class='option roboto-medium ng-scope'][translate='Sign_out']")
        except:
            self.fail("The account didn't login properly")
        test10.sign_out_button()
        test10.click_user_icon()
        try:
            self.driver.find_element_by_id("sign_in_btnundefined").text
        except:
            self.fail("the sign in button couldn't be found, therefore the account hasn't logged out properly' ")

        # option 2 - this option follows the instruction of using the UnitTest tse methods (assertions)
        # irrelevant as for the "assertion" itself could not fail, only the "find.element" inside the assertion can fail
        # self.assertEqual("SIGN IN", self.driver.find_element_by_id("sign_in_btnundefined").text)

