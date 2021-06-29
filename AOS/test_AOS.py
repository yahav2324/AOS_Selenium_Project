from unittest import TestCase
from selenium import webdriver
from AOS.AOS_POM import init_Actions_AOS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class TestAOS(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\selenium\chromedriver.exe')
        # self.driver = webdriver.Chrome(executable_path=r'C:\Users\itama\Desktop\selenium\chromedriver.exe')
        self.driver.implicitly_wait(15)
        self.driver.get('https://www.advantageonlineshopping.com/#/')
        self.driver.maximize_window()
        self.driver.refresh()
        # no user is active
        # init_Actions_AOS(self.driver).login('lol1234', 'Lol1234')
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.ID, "headphonesTxt")))

    def tearDown(self):
        self.driver.close()

    def test1(self):
        # add a product with quantity = 2
        test1 = init_Actions_AOS(self.driver)
        test1.enter_category_from_homepage("headphones")
        test1.choose_product_from_current_category_page("12")
        test1.choose_prod_color("GRAY")
        test1.add_quantity_and_click_add("2")

        # add a second product with quantity = 3
        test1.click_back()
        test1.choose_product_from_current_category_page("15")
        test1.choose_prod_color("BLACK")
        test1.add_quantity_and_click_add("3")

        # check that cart icon appears with 5 products (quantity in total)
        self.assertIn("5 Items", test1.total_quan_of_products_in_cart())  # new

    def test2(self):
        # add a product with quantity = 3
        test2 = init_Actions_AOS(self.driver)
        test2.enter_category_from_homepage("laptops")
        test2.choose_product_from_current_category_page("10")
        name1 = self.driver.find_element_by_css_selector("h1[class='roboto-regular ng-binding']").text
        test2.choose_prod_color("GRAY")  # new
        test2.add_quantity_and_click_add("3")

        # add a second product with quantity = 2
        test2.click_back()
        test2.choose_product_from_current_category_page("7")
        name2 = self.driver.find_element_by_css_selector("h1[class='roboto-regular ng-binding']").text
        test2.choose_prod_color("GRAY")  # new
        test2.add_quantity_and_click_add("2")

        # add a third product with quantity = 2
        test2 = init_Actions_AOS(self.driver)
        test2.back_to_homepage()
        test2.enter_category_from_homepage("mice")
        test2.choose_product_from_current_category_page("30")
        name3 = self.driver.find_element_by_css_selector("h1[class='roboto-regular ng-binding']").text
        test2.choose_prod_color("RED")  # new
        test2.add_quantity_and_click_add("2")

        # check all products added successfully
        names = self.driver.find_elements_by_css_selector("h3[class='ng-binding']")
        quantities = self.driver.find_elements_by_xpath("//a/label[@class = 'ng-binding'][1]")
        colors = self.driver.find_elements_by_css_selector("span[class='ng-binding']")
        product3 = f"{names[0].text}: quantity is {quantities[0].text}, color is {colors[0].text} "
        product2 = f"{names[1].text}: quantity is {quantities[1].text}, color is {colors[1].text} "
        product1 = f"{names[2].text}: quantity is {quantities[2].text}, color is {colors[2].text} "
        # product 1
        self.assertIn(name1, product1); self.assertIn("3", product1); self.assertIn("GRAY", product1)
        self.assertIn(name2, product2); self.assertIn("2", product2); self.assertIn("GRAY", product2)
        self.assertIn(name3, product3); self.assertIn("2", product3); self.assertIn("RED", product3)


    def test3(self):
        # add a product with quantity of 2
        test3 = init_Actions_AOS(self.driver)
        test3.enter_category_from_homepage("speakers")
        test3.choose_product_from_current_category_page("20")
        product1 = self.driver.find_element_by_css_selector('h1[class="roboto-regular screen768 ng-binding"]').text
        test3.choose_prod_color("BLACK")
        test3.add_quantity_and_click_add("2")

        # add a product with quantity of 3
        test3.click_back()
        test3.choose_product_from_current_category_page("25")
        product2 = self.driver.find_element_by_css_selector('h1[class="roboto-regular screen768 ng-binding"]').text
        test3.choose_prod_color("RED")
        test3.add_quantity_and_click_add("3")

        # remove the last product added
        test3.point_on_cart_icon() # new
        self.driver.find_element_by_xpath('//ul/li/tool-tip-cart/div/table/tbody/tr[1]/td/div/' 
                                                  'div[@class="removeProduct iconCss iconX"]').click()
        sleep(3)
        # self.driver.find_element_by_class_name("removeProduct iconCss iconX").click()

        # check that only the first product is left in cart
        self.assertNotIn(product2[0:25], self.driver.find_element_by_css_selector("h3[class='ng-binding']").text)
        self.assertIn(product1[0:25], self.driver.find_element_by_css_selector("h3[class='ng-binding']").text)

    def test4(self):
        test4 = init_Actions_AOS(self.driver)
        test4.enter_category_from_homepage("tablets")
        test4.choose_product_from_current_category_page("16")
        test4.choose_prod_color("GRAY")
        test4.add_quantity_and_click_add("3")
        test4.cart_page()
        self.assertEqual(self.driver.find_element_by_css_selector("[class='select  ng-binding']").text, "SHOPPING CART")

    def test5(self):
        # add a product with quantity = 3
        test5 = init_Actions_AOS(self.driver)
        test5.enter_category_from_homepage("laptops")
        test5.choose_product_from_current_category_page("10")
        price1 = test5.calculate_product_price_with_quantity("3")
        test5.choose_prod_color("GRAY")

        test5.add_quantity_and_click_add("3")

        # add a second product with quantity = 2
        test5.click_back()
        test5.choose_product_from_current_category_page("7")
        price2 = test5.calculate_product_price_with_quantity("2")
        test5.add_quantity_and_click_add("2")

        # add a third product with quantity = 2
        test5 = init_Actions_AOS(self.driver)
        test5.back_to_homepage()
        test5.enter_category_from_homepage("mice")
        test5.choose_product_from_current_category_page("30")
        price3 = test5.calculate_product_price_with_quantity("2")
        test5.add_quantity_and_click_add("2")

        # move to cart page
        test5.cart_page()

        # converting the prices to a final price in money format
        sum_prices = price1+price2+price3
        sum_prices = test5.convert_number_into_money_dollar_format(sum_prices)

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
        sleep(5)
        # edit product 1
        init_Actions_AOS(self.driver).edit_products(2)
        # check after the product changed, if the cart will be changed accordingly
        products = init_Actions_AOS(self.driver).return_quantity_cart_products(2)
        print(f"products: {products}")
        self.assertIn('6', products[0])
        self.assertIn('7', products[1])


    def test7(self):
                # choose a product 1
                init_Actions_AOS(self.driver).enter_category_from_homepage('tablets')
                init_Actions_AOS(self.driver).choose_product_from_current_category_page('18')
                init_Actions_AOS(self.driver).choose_prod_color('GRAY')
                init_Actions_AOS(self.driver).add_quantity_and_click_add("5")
                # return category page by navigation bar
                init_Actions_AOS(self.driver).click_back()
                # check if the current page is a tablet category
                text_tablets = init_Actions_AOS(self.driver).element_in_tablet_category_page()
                self.assertEqual('TABLETS', text_tablets)
                # check if the current page is a homepage
                init_Actions_AOS(self.driver).click_back()
                text_in_homep = init_Actions_AOS(self.driver).element_in_homepage()
                self.assertEqual('HEADPHONES', text_in_homep)

            # def test7_2(self):

    def test8(self):
        init_Actions_AOS(self.driver).wait_homepage_loading()
        init_Actions_AOS(self.driver).enter_category_from_homepage('mice')
        init_Actions_AOS(self.driver).choose_product_from_current_category_page('27')
        init_Actions_AOS(self.driver).choose_prod_color('PURPLE')
        init_Actions_AOS(self.driver).add_quantity_and_click_add('3')
        init_Actions_AOS(self.driver).point_on_cart_icon()
        init_Actions_AOS(self.driver).click_checkout_button()
        init_Actions_AOS(self.driver).wait_order_payment_page_loading()
        init_Actions_AOS(self.driver).register('lol56', 'Lol41', 'Lol41', 'lol71@gmail.com')  # new
        init_Actions_AOS(self.driver).wait_order_payment_page_loading()
        init_Actions_AOS(self.driver).click_next_button_shipdetails_page()
        init_Actions_AOS(self.driver).wait_payment_method_page_loading()
        init_Actions_AOS(self.driver).choose_safepay_payment_method('ya112', 'Ya11')  # new
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
        sleep(5)
        all_orders = init_Actions_AOS(self.driver).my_orders()
        print(all_orders)
        self.assertIn(id_order, all_orders)

    def test9(self):
        init_Actions_AOS(self.driver).enter_category_from_homepage('tablets')
        init_Actions_AOS(self.driver).choose_product_from_current_category_page('18')
        init_Actions_AOS(self.driver).choose_prod_color('GRAY')
        init_Actions_AOS(self.driver).add_quantity_and_click_add("5")

        init_Actions_AOS(self.driver).point_on_cart_icon()
        init_Actions_AOS(self.driver).click_checkout_button()
        init_Actions_AOS(self.driver).wait_order_payment_page_loading()

        init_Actions_AOS(self.driver).login_from_order_payment_page('lol1234', 'Lol1234')
        init_Actions_AOS(self.driver).wait_order_payment_page_loading()
        init_Actions_AOS(self.driver).click_next_button_shipdetails_page()
        init_Actions_AOS(self.driver).wait_order_payment_page_loading()
        init_Actions_AOS(self.driver).choose_mastercredit_payment_method('234554322142',
                                                                         '122', '10', '2023', 'jone ver')
        init_Actions_AOS(self.driver).wait_thank_page_appear()
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
        test10.login("lol1234", "Lol1234")
        sleep(2)
        test10.click_user_icon()
        sign_out_button = self.driver.find_element_by_css_selector(
            "[class='option roboto-medium ng-scope'][translate='Sign_out']")
        self.assertIn("Sign out", sign_out_button.text)

        test10.sign_out_button()
        test10.click_user_icon()
        # option 1
        try:
            self.driver.find_element_by_id("sign_in_btnundefined").text
        except:
            self.fail("the sign in button couldn't be found, therefore the account hasn't logged out properly' ")

        # option 2 - this option follows the instruction of using the UnitTest tse methods (assertions)
        # irrelevant as for the "assertion" itself could not fail, only the "find.element" inside the assertion can fail
        # self.assertEqual("SIGN IN", self.driver.find_element_by_id("sign_in_btnundefined").text)

