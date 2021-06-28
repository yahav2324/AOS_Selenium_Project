from unittest import TestCase
from selenium import webdriver
from AOS.AOS_POM import init_Actions_AOS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestAOS(TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path=r'C:\selenium\chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\itama\Desktop\selenium\chromedriver.exe')
        self.driver.implicitly_wait(1000000)
        self.driver.get('https://www.advantageonlineshopping.com/#/')
        self.driver.maximize_window()
        # no user is active
        init_Actions_AOS(self.driver).login('lol1234', 'Lol1234')
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.ID, "headphonesTxt")))

    def tearDown(self):
        self.driver.close()

    def test1(self):
        # add a product with quantity = 2
        test1 = init_Actions_AOS(self.driver)
        test1.enter_category_from_homepage("headphones")
        test1.choose_product_from_current_category_page("12")
        test1.choose_prod_color("")
        test1.add_quantity_and_click_add("2")

        # add a second product with quantity = 3
        test1.back_to_category_page()
        test1.choose_product_from_current_category_page("15")
        test1.choose_prod_color("")
        test1.add_quantity_and_click_add("3")

        # check that cart icon appears with 5 products (quantity in total)
        self.assertEqual(test1.total_quan_of_products_in_cart(), "5 Items")

    def test2(self):
        # add a product with quantity = 3
        test2 = init_Actions_AOS(self.driver)
        test2.enter_category_from_homepage("laptops")
        test2.choose_product_from_current_category_page("10")
        name1 = self.driver.find_element_by_css_selector("h1[class='roboto-regular ng-binding']")
        test2.choose_prod_color("")
        test2.add_quantity_and_click_add("3")

        # add a second product with quantity = 2
        test2.back_to_category_page()
        test2.choose_product_from_current_category_page("7")
        name2 = self.driver.find_element_by_css_selector("h1[class='roboto-regular ng-binding']")
        test2.choose_prod_color("")
        test2.add_quantity_and_click_add("2")

        # add a third product with quantity = 2
        test2 = init_Actions_AOS(self.driver)
        test2.back_to_homepage()
        test2.enter_category_from_homepage("mice")
        test2.choose_product_from_current_category_page("30")
        name3 = self.driver.find_element_by_css_selector("h1[class='roboto-regular ng-binding']")
        test2.choose_prod_color("")
        test2.add_quantity_and_click_add("2")

        # check all products added successfully
        names = self.driver.find_elements_by_css_selector("h3[class='ng-binding']")
        quantity_and_color = self.driver.find_elements_by_xpath("//a/label[@class = 'ng-binding']")
        product3 = f"{names[0].text}: quantity is {quantity_and_color[0]}, color is {quantity_and_color[1]} "
        product2 = f"{names[1].text}: quantity is {quantity_and_color[2]}, color is {quantity_and_color[3]} "
        product1 = f"{names[2].text}: quantity is {quantity_and_color[4]}, color is {quantity_and_color[5]} "
        self.assertIn(name1, product1);
        self.assertIn()

    def test3(self):
        # add a product with quantity of 2
        test3 = init_Actions_AOS(self.driver)
        test3.enter_category_from_homepage("speakers")
        test3.choose_product_from_current_category_page("20")
        product1 = self.driver.find_element_by_css_selector("h1[class='roboto-regular ng-binding']").text
        test3.choose_prod_color("")
        test3.add_quantity_and_click_add("2")

        # add a product with quantity of 3
        test3.back_to_category_page()
        test3.choose_product_from_current_category_page("25")
        product2 = self.driver.find_element_by_css_selector("h1[class='roboto-regular ng-binding']").text
        test3.choose_prod_color("")
        test3.add_quantity_and_click_add("3")

        # remove the last product added
        self.driver.find_element_by_class_name("removeProduct iconCss iconX").click()

        # check that only the first product is left in cart
        self.assertNotIn(product2, self.driver.find_element_by_css_selector("h3[class='ng-binding']").text)
        self.assertIn(product1, self.driver.find_element_by_css_selector("h3[class='ng-binding']").text)

    def test4(self):
        test4 = init_Actions_AOS(self.driver)
        test4.enter_category_from_homepage("tablets")
        test4.choose_product_from_current_category_page("16")
        test4.choose_prod_color("")
        test4.add_quantity_and_click_add("3")
        test4.cart_page()
        self.assertEqual(self.driver.find_element_by_css_selector("[class='select  ng-binding']").text, "SHOPPING CART")

    def test5(self):
        # add a product with quantity = 3
        test5 = init_Actions_AOS(self.driver)
        test5.enter_category_from_homepage("laptops")
        test5.choose_product_from_current_category_page("10")
        test5.choose_prod_color("")
        test5.add_quantity_and_click_add("3")

        # add a second product with quantity = 2
        test5.back_to_category_page()
        test5.choose_product_from_current_category_page("7")
        test5.add_quantity_and_click_add("2")

        # add a third product with quantity = 2
        test5 = init_Actions_AOS(self.driver)
        test5.back_to_homepage()
        test5.enter_category_from_homepage("mice")
        test5.choose_product_from_current_category_page("30")
        test5.add_quantity_and_click_add("2")

        # move to cart page
        test5.cart_page()

        # summing the prices of the products
        self.assertIn(str(test5.calculate_sum_price_of_cart), self.driver.find_element_by_css_selector(
            "#shoppingCart > table > tfoot > tr:nth-child(1) > td:nth-child(2) > span.roboto-medium.ng-binding").text)

        # printing all cart products info
        test5.return_info_cart_products(3)

    def test6(self):
        """The quantity of the product will be change and the quantity of the product
         in the cart page will be Changed accordingly"""
        # choose a product 1
        init_Actions_AOS(self.driver).enter_category_from_homepage('speakers')
        init_Actions_AOS(self.driver).choose_product_from_current_category_page('25')
        init_Actions_AOS(self.driver).choose_prod_color('BLACK')
        init_Actions_AOS(self.driver).add_quantity_and_click_add("3")
        # return home page by navigation bar
        init_Actions_AOS(self.driver).back_to_homepage()
        # waiting for loading home page
        init_Actions_AOS(self.driver).wait_homepage_loading()
        # choose a product 2
        init_Actions_AOS(self.driver).enter_category_from_homepage('tablets')
        init_Actions_AOS(self.driver).choose_product_from_current_category_page('17')
        init_Actions_AOS(self.driver).choose_prod_color('GRAY')
        init_Actions_AOS(self.driver).add_quantity_and_click_add("5")
        # Enter to cart page
        init_Actions_AOS(self.driver).cart_page()
        # edit product 1
        init_Actions_AOS(self.driver).edit_products()
        # check after the product changed, if the cart will be changed accordingly
        products = init_Actions_AOS(self.driver).return_quantity_cart_products(2)
        self.assertIn('1', products[1])
        self.assertIn('2', products[2])

    def test7(self):
        # choose a product 1
        init_Actions_AOS(self.driver).enter_category_from_homepage('tablets')
        init_Actions_AOS(self.driver).choose_product_from_current_category_page('18')
        init_Actions_AOS(self.driver).choose_prod_color('GRAY')
        init_Actions_AOS(self.driver).add_quantity_and_click_add("5")
        # return category page by navigation bar
        init_Actions_AOS(self.driver).back_to_category_page()
        # check if the current page is a tablet category
        text_tablets = init_Actions_AOS(self.driver).element_in_tablet_category_page()
        self.assertEqual('TABLETS', text_tablets)
        # check if the current page is a homepage
        init_Actions_AOS(self.driver).back_to_homepage()
        text_in_homep = init_Actions_AOS(self.driver).element_in_homepage()
        self.assertEqual('HEADPHONES', text_in_homep)

    # def test7_2(self):

    def test8(self):
        init_Actions_AOS(self.driver).click_user_icon()
        init_Actions_AOS(self.driver).sign_out_button()
        init_Actions_AOS(self.driver).wait_homepage_loading()
        init_Actions_AOS(self.driver).enter_category_from_homepage('mice')
        init_Actions_AOS(self.driver).choose_product_from_current_category_page('27')
        init_Actions_AOS(self.driver).choose_prod_color('PURPLE')
        init_Actions_AOS(self.driver).add_quantity_and_click_add('3')
        init_Actions_AOS(self.driver).point_on_cart_icon()
        init_Actions_AOS(self.driver).click_checkout_button()
        init_Actions_AOS(self.driver).wait_order_payment_page_loading()
        init_Actions_AOS(self.driver).register('lol51', 'Lol41', 'Lol41', 'lol51@gmail.com')
        init_Actions_AOS(self.driver).wait_order_payment_page_loading()
        init_Actions_AOS(self.driver).click_next_button_shipdetails_page()
        init_Actions_AOS(self.driver).wait_payment_method_page_loading()
        init_Actions_AOS(self.driver).choose_safepay_payment_method('ya11', 'Ya11')
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

    def test9(self):
        init_Actions_AOS(self.driver).click_user_icon()
        init_Actions_AOS(self.driver).sign_out_button()
        init_Actions_AOS(self.driver).wait_homepage_loading()

        init_Actions_AOS(self.driver).enter_category_from_homepage('tablets')
        init_Actions_AOS(self.driver).choose_product_from_current_category_page('18')
        init_Actions_AOS(self.driver).choose_prod_color('GRAY')
        init_Actions_AOS(self.driver).add_quantity_and_click_add("5")

        init_Actions_AOS(self.driver).point_on_cart_icon()
        init_Actions_AOS(self.driver).click_checkout_button()
        init_Actions_AOS(self.driver).wait_order_payment_page_loading()

        init_Actions_AOS(self.driver).login_from_order_payment_page('lol123', 'Lol123')
        init_Actions_AOS(self.driver).wait_order_payment_page_loading()
        init_Actions_AOS(self.driver).click_next_button_shipdetails_page()
        init_Actions_AOS(self.driver).choose_mastercredit_payment_method('234554322345',
                                                                         '312', '12', '2022', 'jone ver')
        id_order = init_Actions_AOS(self.driver).order_number_in_thank_page()

        init_Actions_AOS(self.driver).cart_page()
        empty_cart = init_Actions_AOS(self.driver).appear_text_cart_empty()
        self.assertEqual('Your shopping cart is empty', empty_cart)

        init_Actions_AOS(self.driver).click_user_icon()
        init_Actions_AOS(self.driver).click_my_orders()
        all_orders = init_Actions_AOS(self.driver).my_orders()
        self.assertIn(id_order, all_orders)

    def test10(self):
        test10 = init_Actions_AOS(self.driver)
        test10.login("lol123", "Lol123")
        test10.click_user_icon()
        sign_out_button = self.driver.find_element_by_css_selector(
            "[class='option roboto-medium ng-scope'][translate='Sign_out']")
        self.assertIn("Sign out", sign_out_button.text)

        test10.sign_out_button()
        test10.click_user_icon()
        # option 1
        try:
            self.driver.find_element_by_id(self.driver.find_element_by_id("sign_in_btnundefined").text)
        except:
            self.fail("the sign in button couldn't be found, therefore the account hasn't logged out properly' ")

        # option 2 - this option follows the instruction of using the UnitTest tse methods (assertions)
        # irrelevant as for the "assertion" itself could not fail, only the "find.element" inside the assertion can fail
        # self.assertEqual("SIGN IN", self.driver.find_element_by_id("sign_in_btnundefined").text)

