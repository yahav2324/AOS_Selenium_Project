from unittest import TestCase
from selenium import webdriver
from AOSֹֹֹ_ITAMAR.AOS_POM import init_Actions_AOS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep



class test1_AOS(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\itama\Desktop\selenium\chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.driver.get('https://www.advantageonlineshopping.com/#/')
        self.driver.maximize_window()
        # no user is active
        init_Actions_AOS(self.driver).login('lol1234', 'Lol1234')
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.ID, "headphonesTxt")))

    def tearDown(self):
        sleep(4)
        self.driver.close()

    def test1(self):

        # add a product with quantity = 2
        test1 = init_Actions_AOS(self.driver)
        test1.enter_category_from_homepage("headphones")
        test1.choose_product_from_current_category_page("12")
        test1.add_quantity("2")

        # add a second product with quantity = 3
        test1.back_to_category_page()
        test1.choose_product_from_current_category_page("15")
        test1.add_quantity("3")

        # check that cart icon appears with 5 products (quantity in total)
        self.assertEqual(test1.total_quan_of_products_in_cart(), "5 Items")

    def test2(self):

        # add a product with quantity = 3
        test2 = init_Actions_AOS(self.driver)
        test2.enter_category_from_homepage("laptops")
        test2.choose_product_from_current_category_page("10")
        name1 = self.driver.find_element_by_css_selector("h1[class='roboto-regular ng-binding']")
        test2.add_quantity("3")

        # add a second product with quantity = 2
        test2.back_to_category_page()
        test2.choose_product_from_current_category_page("7")
        name2 = self.driver.find_element_by_css_selector("h1[class='roboto-regular ng-binding']")
        test2.add_quantity("2")

        # add a third product with quantity = 2
        test2 = init_Actions_AOS(self.driver)
        test2.back_to_homepage()
        test2.enter_category_from_homepage("mice")
        test2.choose_product_from_current_category_page("30")
        name3 = self.driver.find_element_by_css_selector("h1[class='roboto-regular ng-binding']")
        test2.add_quantity("2")

        # check all products added successfully
        names = self.driver.find_elements_by_css_selector("h3[class='ng-binding']")
        quantity_and_color = self.driver.find_elements_by_xpath("//a/label[@class = 'ng-binding']")
        product3 = f"{names[0]}: quantity is {quantity_and_color[0]}, color is {quantity_and_color[1]} "
        product2 = f"{names[1]}: quantity is {quantity_and_color[2]}, color is {quantity_and_color[3]} "
        product1 = f"{names[2]}: quantity is {quantity_and_color[4]}, color is {quantity_and_color[5]} "
        self.assertIn(name1, product1); self.assertIn()


    def test3(self):

        # add a product with quantity of 2
        test3 = init_Actions_AOS(self.driver)
        test3.enter_category_from_homepage("speakers")
        test3.choose_product_from_current_category_page("20")
        product1 = self.driver.find_element_by_css_selector("h1[class='roboto-regular ng-binding']").text
        test3.add_quantity("2")

        # add a product with quantity of 3
        test3.back_to_category_page()
        test3.choose_product_from_current_category_page("25")
        product2 = self.driver.find_element_by_css_selector("h1[class='roboto-regular ng-binding']").text
        test3.add_quantity("3")

        # remove the last product added
        self.driver.find_element_by_class_name("removeProduct iconCss iconX").click()

        # check that only the first product is left in cart
        self.assertNotIn(product2, self.driver.find_element_by_css_selector("h3[class='ng-binding']").text)
        self.assertIn(product1, self.driver.find_element_by_css_selector("h3[class='ng-binding']").text)

    def test4(self):
        test4 = init_Actions_AOS(self.driver)
        test4.enter_category_from_homepage("tablets")
        test4.choose_product_from_current_category_page("16")
        test4.add_quantity("3")
        test4.cart_page()
        self.assertEqual(self.driver.find_element_by_css_selector("[class='select  ng-binding']").text, "SHOPPING CART")

    def test5(self):
        test5 = init_Actions_AOS(self.driver)
        # add a product with quantity = 3
        test5 = init_Actions_AOS(self.driver)
        test5.enter_category_from_homepage("laptops")
        test5.choose_product_from_current_category_page("10")
        test5.add_quantity("3")

        # add a second product with quantity = 2
        test5.back_to_category_page()
        test5.choose_product_from_current_category_page("7")
        test5.add_quantity("2")

        # add a product with quantity = 2
        test5 = init_Actions_AOS(self.driver)
        test5.back_to_homepage()
        test5.enter_category_from_homepage("mice")
        test5.choose_product_from_current_category_page("30")
        test5.add_quantity("2")

        # move to cart page
        test5.cart_page()

        # summing the prices of the products
        self.assertIn(str(test5.calculate_sum_price_of_cart), self.driver.find_element_by_css_selector("#shoppingCart > table > tfoot > tr:nth-child(1) > td:nth-child(2) > span.roboto-medium.ng-binding").text)

        # printing all cart products info
        test5.return_cart_products(3)



